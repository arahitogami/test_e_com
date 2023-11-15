import functools
from abc import abstractmethod, ABC

import phonenumbers
from datetime import datetime
from typing import Dict, Union

from pydantic import (BaseModel, validate_email, Field, ConfigDict,
                      model_validator)


class TypeValue(str, ABC):
    @property
    @abstractmethod
    def text_error(self):
        pass

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @staticmethod
    def error_validator(func):
        @functools.wraps(func)
        def wrapper(cls, v, field: Field):
            try:
                result = func(cls, v, field)
                if result:
                    return result
            except Exception:
                raise ValueError(cls.text_error)
            else:
                raise ValueError(cls.text_error)

        return wrapper

    @classmethod
    @error_validator
    def validate(cls, v, field: Field):
        return cls.checking_parameters(v)

    @staticmethod
    @abstractmethod
    def checking_parameters(v):
        pass


class Date(TypeValue):
    text_error = "Строка не является датой формата "\
                 "DD.MM.YYYY или YYYY-MM-DD."

    @staticmethod
    def checking_parameters(v):
        for format_date in ["%d.%m.%Y", "%Y-%m-%d"]:
            try:
                date = datetime.strptime(v, format_date)
            except Exception:
                continue
            if date:
                return "date"


class PhoneNumber(TypeValue):
    text_error = ("Строка не является номером телефона "
                  "формата +7 xxx xxx xx xx.")

    @staticmethod
    def checking_parameters(v):
        parsed_number = phonenumbers.parse(v, "RU")
        if phonenumbers.is_valid_number(parsed_number):
            return "phone"

        # Так как пакет phonenumbers валидирует разные варианты передачи номера
        # то укажу другую проверку в комментариях, можно еще и регулярку взять
        # TODO раскомментировать если телефон нужен строго формата +79609609999
        # if v[:2] == '+7' and int(v[2:]) and len(v[2:]) == 10:
        #     return "phone"


class Email(TypeValue):
    text_error = "Строка не является электронным адресом."

    @staticmethod
    def checking_parameters(v):
        name, email = validate_email(v)
        if name and email:
            return "email"


class Text(TypeValue):
    text_error = "Строка не является текстом."

    @staticmethod
    def checking_parameters(v):
        if type(v) is str:
            return "text"
        else:
            raise Exception


class DataItem(BaseModel):
    data: Dict[str, Union[Date, PhoneNumber, Email, Text]]


class Items(BaseModel):
    model_config = ConfigDict(extra='allow')

    @model_validator(mode='before')
    def validate_all(cls, values: dict):
        if values.get('name'):
            raise ValueError('Нельзя передавать поле с именем "name".')
        elif values.get('_id'):
            raise ValueError('Нельзя передавать поле с именем "name".')
        return DataItem(data=values).data
