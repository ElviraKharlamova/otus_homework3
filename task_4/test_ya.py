import pytest
import requests

def test_check_ya(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code


@pytest.mark.parametrize("id", ["randomrandom", 55, 0, -1])
def negative_test_ya(base_url, id, status_code_error):
    response = requests.get(f"{base_url}/{id}")
    assert response.status_code == status_code_error
