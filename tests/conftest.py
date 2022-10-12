import pytest
import requests
from utils.file_reader import read_file

@pytest.fixture(scope="module")
def l_oppfi_offer_url(g_target_url):
    '''
        returns /offer endpoint url
    '''
    return g_target_url + "/offer"

@pytest.fixture
def l_payload():
    payload = read_file('offer_application.json')
    return payload
