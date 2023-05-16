import pytest
import requests


def test_get_users_status_code_200(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200

def test_check_quantity_post_100(base_url):
    response = requests.get(f"{base_url}/posts")
    assert len(response.json()) == 100
    assert response.status_code == 200

def test_check_quantity_photos_5000(base_url):
    response = requests.get(f"{base_url}/photos")
    assert len(response.json()) == 5000
    assert response.status_code == 200

@pytest.mark.parametrize("postId", [1, 5, 7])
def test_get_comments_status_code_200(postId, base_url):
    response = requests.get(f"{base_url}/comments?postId={postId}")
    assert response.status_code == 200
    comments_in_postid = response.json()
    for comment in comments_in_postid:
        assert comment["postId"] == postId


@pytest.mark.parametrize("post", [1, 2,7])
def test_delete_post(post, base_url):
    response = requests.delete(f"{base_url}/posts/{post}")
    assert response.status_code == 200