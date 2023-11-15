from copy import deepcopy

import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from db import MONGODB_URL
from tests.fixture_form_template import templates, forms_for_template


@pytest.fixture
async def override_create_test_db():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client.test_databse
    db['template'].insert_many(deepcopy(templates))
    yield db
    db['template'].drop()
    client.close()


async def test_form_template(
        ac: AsyncClient,
        override_create_test_db: AsyncIOMotorDatabase
):
    for form_type, form in forms_for_template.items():
        for f in form:
            response = await ac.post(
                "/get_form/",
                json=f[0]
            )
            if form_type == "good_template":
                assert response.status_code == 200, response.json()
                right_result = {
                    k: v for k, v in f[1].items() if k not in [
                        'new_name_1', 'new_name_2'
                    ]
                }
                assert response.json() == right_result
            elif form_type == "new_template":
                assert response.status_code == 200
                assert response.json() == f[1]
            elif form_type == "bad_template":
                assert response.status_code == 422
