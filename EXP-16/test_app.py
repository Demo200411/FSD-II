import pytest # type: ignore
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_add_success(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 5

def test_add_invalid(client):
    response = client.get("/add?a=x&b=3")
    assert response.status_code == 400
    assert "error" in response.json