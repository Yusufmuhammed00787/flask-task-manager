
import pytest
from app import app, tasks


@pytest.fixture
def client():
    app.config["TESTING"] = True
    tasks.clear()

    with app.test_client() as client:
        yield client

    tasks.clear()


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"My Task Manager" in response.data


def test_add_task(client):
    response = client.post(
        "/add",
        data={"task": "Learn Jenkins"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Learn Jenkins" in response.data
    assert len(tasks) == 1


def test_complete_task(client):
    client.post("/add", data={"task": "Learn Docker"})

    response = client.post(
        "/complete/0",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert tasks[0]["done"] is True
