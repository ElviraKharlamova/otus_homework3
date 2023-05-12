import pytest
import requests



def test_list_dog_breeds(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    print(response.json())

@pytest.mark.parametrize("number", [1, 3, 11, 42, 50, pytest.param(51, marks=pytest.mark.xfail)])
def test_random_numbers_image(number, base_url):
    image = f"{base_url}/breeds/image/random/{number}"
    image_dogs = requests.get(image)
    assert len(image_dogs.json().get("message")) == number

@pytest.mark.parametrize("number", [50, 51, 99, 555])
def test_limit_50(number, base_url):
    limit_num = f"{base_url}/breeds/image/random/{number}"
    image_limit = requests.get(limit_num)
    assert len(image_limit.json().get("message")) == 50

@pytest.mark.parametrize("breed_name, status_code", [("akita", 200)])
def test_dog_breed_image(breed_name, status_code,base_url):
    response = requests.get(f"{base_url}/breed/{breed_name}/images/random")
    assert response.status_code == status_code

@pytest.mark.parametrize("sub_breed_name, status_code, number", [("afghan", 200, 3)])
def test_dog_sub_breed_image(sub_breed_name, status_code, number,base_url):
    response = requests.get(f"{base_url}/breed/hound/{sub_breed_name}/images/random/{number}")
    assert response.status_code == status_code