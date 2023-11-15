from typing import Annotated

from fastapi import FastAPI, Body, Depends

from motor.motor_asyncio import AsyncIOMotorDatabase

from forms_template.database import db_template
from forms_template.shemas import Items
from forms_template.utils import find_document

app = FastAPI(
    title="e.com-test"
)


@app.post("/get_form/", responses=dict())
async def get_form(
        db: Annotated[AsyncIOMotorDatabase, Depends(db_template)],
        items: Annotated[Items, Body()],
):

    return await find_document(db, items.model_dump())
