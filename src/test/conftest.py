import pytest
from faker import Faker
import requests


@pytest.fixture(scope="module")
def g_typicode_url():
    '''
        returns typicode url
    '''
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def g_faker():
    '''
        returns a faker object to be used in test for random
        data generation
    '''
    faker_obj = Faker()
    return faker_obj


@pytest.fixture(scope="module")
def g_posts_url(g_typicode_url):
    '''
        returns full /posts endpoint url
    '''
    return g_typicode_url + "/posts"


@pytest.fixture(scope="module")
def g_posts_by_id(g_posts_url):
    def _g_posts_by_id(post_id, verb="GET", payload=None):
        url = g_posts_url + '/{}'.format(post_id)
        if payload is None:
            return requests.request(verb, url)
        return requests.request(verb, url, json=payload)
    return _g_posts_by_id


@pytest.fixture(scope="module")
def g_post_posts(g_posts_url):
    def _g_post_posts(payload=None):
        if payload is not None:
            return requests.post(g_posts_url, json=payload)
        return requests.post(g_posts_url)
    return _g_post_posts


@pytest.fixture(scope="module")
def g_posts_id_comments(g_posts_url):
    def _g_posts_id_comments(post_id, verb="GET", payload=None):
        url = g_posts_url + '/{}/comments'.format(post_id)
        if payload is None:
            return requests.request(verb, url)
        return requests.request(verb, url, json=payload)
    return _g_posts_id_comments


@pytest.fixture(scope="module")
def g_get_posts(g_posts_url):
    return requests.get(g_posts_url)
