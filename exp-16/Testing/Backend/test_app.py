import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_add(client):
    response = client.get("/add?a=2&b=3")
    
    assert response.status_code == 200
    assert response.json["result"] == 5