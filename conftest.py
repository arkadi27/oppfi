import pytest
import requests
import os
from utils.file_reader import read_file
from config import TARGET_URL, API_KEY

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
