from PIL import Image
import requests

from utils.image_utils import ImageUtils

BASE_URL = "http://127.0.0.1:8000"

imageUtils = ImageUtils()

def test_create_profile():
    response_token = requests.get(f"{BASE_URL}/tokenCSRF/")

    token = response_token.json().get("data")

    img = Image.open("tests/assets/images.png")

    bytes_img = imageUtils.convert_image_to_bytes(img)

    files = {
        "photo": bytes_img
    }

    json = {
        "nickname": "Bruno",
        "description": "Developer",
        "id_user": 1
    }

    response = requests.post(f"{BASE_URL}/profile/", json=json, files=files, headers={"X-CSRFToken": token})

    assert response.status_code == 201
    assert "id" in response.json()