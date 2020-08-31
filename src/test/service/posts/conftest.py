import pytest
import requests


@pytest.fixture(scope="module")
def l_posts_url(g_typicode_url):
    return g_typicode_url + "/posts"


@pytest.fixture(scope="module")
def l_get_posts(l_posts_url):
    return requests.get(l_posts_url)


@pytest.fixture(scope="module")
def l_posts_by_id(l_posts_url):
    def _l_posts_by_id(post_id, verb="GET", payload=None):
        url = l_posts_url + '/{}'.format(post_id)
        if payload is None:
            return requests.request(verb, url)
        return requests.request(verb, url, json=payload)
    return _l_posts_by_id


@pytest.fixture(scope="module")
def l_post_posts(l_posts_url):
    def _l_post_posts(payload=None):
        if payload is not None:
            return requests.post(l_posts_url, json=payload)
        return requests.post(l_posts_url)
    return _l_post_posts
