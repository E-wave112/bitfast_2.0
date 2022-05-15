import pytest
from httpx import AsyncClient
from application import app

@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="https://www.example.com/") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == "welcome to bitfast!, kindly access this url https://bitfast.herokuapp.com/docs to fully explore the API"

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4