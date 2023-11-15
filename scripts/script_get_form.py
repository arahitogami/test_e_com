import asyncio
from typing import Dict, Union

from forms_template.database import db_template
from forms_template.shemas import Items, Date, PhoneNumber, Email, Text
from forms_template.utils import find_document


async def run_script(params: Dict[str, Union[Date, PhoneNumber, Email, Text]]):
    db = await db_template()
    items = Items(**params)
    result = await find_document(db, items.model_dump())
    return result


if __name__ == '__main__':
    params = {
        "field_phone": "+79999999999",
        "field_email": "kjkjfgh@dsfsfd.ty",
        "field_text": "+792311111112",
        "field_date2": "2025-06-17",
    }
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_script(params))
    loop.run_until_complete(future)
    responses = future.result()
    print(responses)
