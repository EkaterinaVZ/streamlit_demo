from fastapi.testclient import TestClient

from main_mask import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "All right, there is a connection."}


def test_post_predict_one():
    response = client.post(
        "/predict/", json={"text": "All [MASK], there is a connection."}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "all alike, there is a connection."


def test_post_predict_two():
    response = client.post("/predict/", json={"text": "I hate [MASK] learning!"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "i hate constantly learning!"


def test_post_predict_three():
    response = client.post("/predict/", json={"text": "I work in [MASK]."})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "i work in hanoi."


def test_post_predict_four():
    response = client.post(
        "/predict/",
        json={"text": "we are [MASK] at the university for the second year."},
    )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "we are now at the university for the second year."
