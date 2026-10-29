from app.main import app


def test_version_endpoint():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json() == {"version": "v1"}