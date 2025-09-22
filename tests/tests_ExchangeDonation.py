import pytest
import requests

@pytest.mark.django_db
def test_ExchangeDonationService():
    BASE_URL = "http://127.0.0.1:8000/api/v1/"

    response = requests.get(BASE_URL + "authentication/csrf-token/")

    assert response.status_code == 200

    csrf_token = response.json().get("csrfToken")

    response = requests.post(BASE_URL + "authentication/login/", 
    headers={"X-CSRFToken": csrf_token},
    json={
        "email": "JhonDoe@gmail.com",
        "password": "Test@123"
    })

    responseExchangeDonation = requests.post(BASE_URL + "exchange-donation-historic/",
    headers={"X-CSRFToken": csrf_token, "Authorization": f"Bearer {response.json().get('access')}"},
    json={
        "user_receiver": 12,
        "id_announce": 6,
        "transaction_type": "exchange",
        "full_name": "Jhon Doe",
        "email": "JhonDoe@gmail.com",
        "password": "Test@123"
    })

    print(responseExchangeDonation.json())

    assert responseExchangeDonation.status_code == 201