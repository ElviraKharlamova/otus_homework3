import pytest
import requests



def test_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

@pytest.mark.parametrize("state_name , number", [("ohio", 3)])
def test_breweries_by_state(state_name, number,base_url):
    response = requests.get(f"{base_url}/breweries?by_state={state_name}&per_page={number}")
    assert response.status_code == 200

@pytest.mark.parametrize("city , number", [("norman", 2)])
def test_breweries_by_city(city, number,base_url):
    response = requests.get(f"{base_url}/v1/breweries?by_city={city}&per_page={number}")
    assert response.status_code == 200

@pytest.mark.parametrize("id", [1, 234])
def test_negative_list(base_url, id):
    url = requests.get(f"{base_url}/breweries/{id}")
    assert url.status_code == 404

@pytest.mark.parametrize("state_name , sort", [("ohio", "asc")])
def test_breweries_by_city(state_name, sort, base_url):
    response = requests.get(f"{base_url}/v1/breweries?by_state=ohio&sort=type,name:{sort}")
    assert response.status_code == 200