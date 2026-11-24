import pytest


@pytest.mark.smoke
def test_get_all_users(api, base_url):
    response = api.get(f"{base_url}/users", timeout=10)
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 10


@pytest.mark.regression
def test_user_email_format(api, base_url):
    users = api.get(f"{base_url}/users", timeout=10).json()
    assert all("@" in user["email"] for user in users)


@pytest.mark.regression
def test_post_comments_belong_to_post(api, base_url):
    response = api.get(f"{base_url}/posts/1/comments", timeout=10)
    assert response.status_code == 200
    comments = response.json()
    assert len(comments) == 5
    assert all(comment["postId"] == 1 for comment in comments)
