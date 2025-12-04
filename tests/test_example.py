import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_root_status_code(client):
    """Root URL should return a 200 OK."""
    response = client.get("/")
    assert response.status_code == 200


def test_root_renders_html(client):
    """Root URL should return HTML content."""
    response = client.get("/")
    # Flask templates normally return HTML strings
    assert response.content_type == "text/html; charset=utf-8"
    assert b"<html" in response.data.lower()  # Basic HTML structure check

