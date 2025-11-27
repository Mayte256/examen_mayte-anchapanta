import json
from app import app

def test_api_route():
    client = app.test_client()
    response = client.get("/api")

    assert response.status_code == 200
    data = json.loads(response.data)

    assert data["status"] == "ok"
    assert "API funcionando" in data["message"]
