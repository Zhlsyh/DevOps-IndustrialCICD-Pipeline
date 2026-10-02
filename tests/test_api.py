from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_get_telemetry_success():
    response = client.get("/telemetry/ESP32_01")
    assert response.status_code == 200
    assert response.json()["temperature"] == 28.5

def test_get_telemetry_not_found():
    response = client.get("/telemetry/UNKNOWN")
    assert response.status_code == 404