import asyncio

from forms_template.database import db_template
from forms_template.shemas import Items
from forms_template.utils import find_document


async def run_script(params: dict):
    db = await db_template()
    items = Items(**params)
    return await find_document(db, items.model_dump())


if __name__ == '__main__':
    params = {
        "field_phone": "+79999999999",
        "field_email": "kjkjfgh@dsfsfd.ty",
        "field_text": "+79231111111",
        "field_date": "01.03.2078",
        "field_date2": "2025-06-17",
    }
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run_script(params))
    loop.run_until_complete(future)
    responses = future.result()
    print(responses)
