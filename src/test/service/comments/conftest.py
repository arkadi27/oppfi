import pytest
import requests


@pytest.fixture(scope="module")
def l_comments_url(g_typicode_url):
    return g_typicode_url + "/comments"


@pytest.fixture(scope="module")
def l_comments_by_postId(l_comments_url):
    def l_comments_by_postId(post_id=None, verb="GET", params=None):
        if params is None:
            return requests.request(verb, l_comments_url)
        return requests.request(verb, l_comments_url, params=params)
    return l_comments_by_postId
