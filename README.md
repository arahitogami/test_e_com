
<!-- ABOUT THE PROJECT -->
## Тестовое задание в е.Ком

Web-приложение для определения заполненных форм.

### **Входные данные для веб-приложения:**
Список полей со значениями в теле POST запроса.
### **Выходные данные:**
Имя наиболее подходящей данному списку полей формы, при отсутствии совпадений с известными формами произвести типизацию полей на лету и вернуть список полей с их типами.


## В разарботке использовались следующие инструменты


* [![Docker][docker.com]][Docker-url]
* [![MongoDB][mongodb.com]][mongodb-url]
* [![FastApi][fastapi.tiangolo.com]][Fastapi-url]
* [![Pydantic][docs.pydantic.dev]][Pydantic-url]
* [![Python][Python.org]][Python-url]
* [![Pytest][docs.pytest.org]][Pytest-url]
* [![Motor][motor.io]][motor-url]

## Предварительные настройки

#### 1) В файле .env есть несколько настраиваемых полей, как показано ниже. Вы можете настроить их в соответствии со своими потребностями.
```
    MONGO_INITDB_ROOT_USERNAME=root
    MONGO_INITDB_ROOT_PASSWORD=example
    MONGO_HOST=mongo
    MONGO_PORT=27017
```
- MONGO_INITDB_ROOT_USERNAME - имя пользователя
- MONGO_INITDB_ROOT_PASSWORD - пароль
- MONGO_HOST - хост указан как имя контейнера
- MONGO_PORT - порт контейнера

#### 2) Перед запуском сервера вы можете проверить работоспособность кода. Для этого сначала установите все пакеты из файла requirements.txt, запустите контейнер mongo в docker-compose и дождитесь его поднятия. А после выполните команду pytest.

```bash
    pip install -r .\requirements.txt
    docker-compose up mongo
    или
    docker-compose up mongo -d
    pytest
```

#### 3) Скрипт run_script находится в файле ./scripts/script_get_form.py

#### 4) В файле ./forms_template/shemas.py есть TODO в классе PhoneNumber. Так как для проверки номера телефона используется пакет phonenumbers, то он может проверять разные варианты номера телефона. Поэтому там есть закомментированная иная проверка, если необходимо строгое соответствие формату, то в функции checking_parameters закомментировать действующие строки, а другие строки раскомментировать.


## Запуск
 

1. Скопируйте репозиторий
   ```bash
   git clone https://github.com/arahitogami/test_e_com.git
   ```
2. В корневой директории проекта выполнить команду
   ```
   docker-compose up --build
   ```
3. Основная и единственная url находится по адресу 

- <http://127.0.0.1:8000/get_form/>
  


## Author
[Kuzmenko Nikita](https://github.com/arahitogami)

## P.S.
На заметку тем, кто будет смотреть это тестовое задание. 
Обратной связи от компании (Code Review) не поступало, поэтому я не знаю, насколько хорошо или плохо было выполнено задание.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[fastapi.tiangolo.com]: https://img.shields.io/badge/FastAPI-0.104.1-green?style=plastic&logo=FastAPI
[Fastapi-url]: https://fastapi.tiangolo.com
[Python.org]: https://img.shields.io/badge/Python-3.11.0-green?style=plastic&logo=python
[Python-url]: https://python.org
[motor.io]: https://img.shields.io/badge/motor-3.3.1-green?style=plastic&logo=motor
[motor-url]: https://motor.readthedocs.io 
[mongodb.com]: https://img.shields.io/badge/mongodb-7.0.4~rc0-green?style=plastic&logo=mongodb
[mongodb-url]: https://www.mongodb.com
[docs.pytest.org]: https://img.shields.io/badge/Pytest-7.4.3-green?style=plastic&logo=pytest
[Pytest-url]: https://docs.pytest.org
[docker.com]: https://img.shields.io/badge/Docker--compose-3.8-green?style=plastic&logo=docker
[Docker-url]: https://docker.com
[docs.pydantic.dev]: https://img.shields.io/badge/Pydantic-2.4.2-green?style=plastic&logo=pydantic
[Pydantic-url]: https://docs.pydantic.dev
