import pytest

REQUIRED_FIELDS = {"userId", "id", "title", "body"}


@pytest.mark.smoke
def test_get_all_posts(api, base_url):
    response = api.get(f"{base_url}/posts", timeout=10)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100


@pytest.mark.smoke
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_single_post(api, base_url, post_id):
    response = api.get(f"{base_url}/posts/{post_id}", timeout=10)
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == post_id
    assert REQUIRED_FIELDS <= set(body.keys())


@pytest.mark.smoke
def test_response_time_under_2_seconds(api, base_url):
    response = api.get(f"{base_url}/posts", timeout=10)
    assert response.elapsed.total_seconds() < 2


@pytest.mark.regression
def test_filter_posts_by_user(api, base_url):
    response = api.get(f"{base_url}/posts", params={"userId": 1}, timeout=10)
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 10
    assert all(post["userId"] == 1 for post in posts)


@pytest.mark.regression
def test_create_post(api, base_url):
    payload = {"title": "pytest post", "body": "created by automation", "userId": 1}
    response = api.post(f"{base_url}/posts", json=payload, timeout=10)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


@pytest.mark.regression
def test_update_post(api, base_url):
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    response = api.put(f"{base_url}/posts/1", json=payload, timeout=10)
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


@pytest.mark.regression
def test_delete_post(api, base_url):
    response = api.delete(f"{base_url}/posts/1", timeout=10)
    assert response.status_code == 200


@pytest.mark.regression
def test_get_nonexistent_post_returns_404(api, base_url):
    response = api.get(f"{base_url}/posts/99999", timeout=10)
    assert response.status_code == 404
