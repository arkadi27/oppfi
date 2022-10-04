import pytest
import requests
import os
from utils.file_reader import read_file
from config import TARGET_URL, API_KEY

'''
def pytest_generate_tests(metafunc):
    os.environ['TARGET_URL'] = 'https://partner-test.opploans.com/api/lde/v4/offer'
    os.environ['API_KEY'] = 'b813b584-6932-4d0a-909f-43ae22df452a'
'''

@pytest.fixture(scope="module")
def g_target_url():
    '''
        returns oppfi target url
    '''
    return TARGET_URL

@pytest.fixture
def g_headers():
    '''
        returns headers
    '''
    return {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
