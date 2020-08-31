import pytest
from faker import Faker


@pytest.fixture(scope="module")
def g_typicode_url():
    '''
        returns typicode url
    '''
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def faker():
    '''
        returns a faker object to be used in test for random
        data generation
    '''
    faker_obj = Faker()
    return faker_obj
