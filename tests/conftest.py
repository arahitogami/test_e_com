import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient

from db import MONGODB_URL
from forms_template.database import db_template
from main import app


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def override_get_db():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client.test_databse
    yield db


app.dependency_overrides[db_template] = override_get_db


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac



