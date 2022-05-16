import pytest
import json
from httpx import AsyncClient
from application import app
from dto.predict import Predict
from utils.crypto_utils import get_crypto_prices
from utils.rand_utils import rand_identifier
from utils.url import get_url


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert (
        response.json()
        == "welcome to bitfast!, kindly access this url https://bitfast.herokuapp.com/docs to fully explore the API"
    )


@pytest.mark.anyio
async def test_prices():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        response = await ac.get("/price")
        assert response.status_code == 200
        assert type(response.json()) == dict


@pytest.mark.anyio
async def test_predict():
    async with AsyncClient(app=app, base_url="https://test") as ac:
        headers = {"content-type": "application/json", "accept": "application/json"}
        params = {"email": "joane@gmail.com"}
        response = await ac.post(
            "/predict", headers=headers, data=json.dumps({"date_entered": "2022-05-16"})
        )
        assert response.status_code == 200
        assert type(response.json()) == dict


def test_crypto_utils():
    assert type(get_crypto_prices()) == dict


def test_rand_utils():
    assert len(rand_identifier()) == 12
    assert type(rand_identifier()) == str


def test_url():
    assert type(get_url()) == str
    assert get_url() == "https://bitfast.herokuapp.com" or "http://127.0.0.1:8000"
