import requests

base_url = "http://localhost:8000"

def test_get_users():
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_assets():
    response = requests.get(f"{base_url}/user_assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_assets():
    response = requests.get(f"{base_url}/assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)