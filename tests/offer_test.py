import pytest
import requests


def test_offer_accepted(l_payload, l_oppfi_offer_url, g_headers):
    """
        GIVEN offer endpoint is up and running
        WHEN a user applies for an offer with correct data
        THEN a 200 status code and correct json response
        is returned.
    """
    response = requests.post(l_oppfi_offer_url, headers = g_headers, json = l_payload)
    rsp_json = response.json()
    # if the first assertion fails, assume allows code execution to continue
    # and report multiple failures if there are any 
    pytest.assume(response.status_code == 200, 'actual status code was {}'.format(response.status_code))
    pytest.assume(rsp_json.get('status') == 'APPROVED')
    pytest.assume(rsp_json.get('request') == l_payload)
    pytest.assume('offers' in rsp_json)
    for offer in rsp_json['offers']:
        pytest.assume('monthlyPayment' in offer)
        pytest.assume('term' in offer)


def test_offer_declined(l_payload, l_oppfi_offer_url, g_headers):
    """
        GIVEN offer endpoint is up and running
        WHEN a user applies for an offer with bad data
        THEN a 200 status code and correct json response
        is returned.
    """
    l_payload['socialSecurityNumber'] = '123450000'
    response = requests.post(l_oppfi_offer_url, headers = g_headers, json = l_payload)
    rsp_json = response.json()
    # if the first assertion fails, assume allows code execution to continue
    # and report multiple failures if there are any 
    pytest.assume(response.status_code == 200, 'actual status code was {}'.format(response.status_code))
    pytest.assume(rsp_json.get('status') == 'DECLINED')
    pytest.assume(rsp_json.get('request') == l_payload)
    pytest.assume('offers' not in response)


@pytest.mark.parametrize("to_remove", ['socialSecurityNumber', 'leadOfferId', 'email', 'stateCode', 'grossMonthlyIncome'])
def test_offer_missing_required_data(to_remove, l_payload, l_oppfi_offer_url, g_headers):
    """
        GIVEN offer endpoint is up and running
        WHEN a user applies for an offer with missing required data
        THEN a 400 status code and correct json response
        is returned.
    """
    del l_payload[to_remove]
    response = requests.post(l_oppfi_offer_url, headers = g_headers, json = l_payload)
    rsp_json = response.json()
    # if the first assertion fails, assume allows code execution to continue
    # and report multiple failures if there are any
    # I am asserting a 400 on purpose because it makes sense to return a bad request status code
    # when a client sends bad data
    pytest.assume(response.status_code == 400, 'actual status code was {}'.format(response.status_code))
    pytest.assume(rsp_json.get('status') == 'DECLINED')
    pytest.assume(rsp_json.get('request') == l_payload)
    pytest.assume('offers' not in response)
    

@pytest.mark.parametrize("operation", ['GET', 'DELETE', 'PUT'])
def test_offer_bad_ops(operation, l_payload, l_oppfi_offer_url, g_headers):
    """
        GIVEN offer endpoint is up and running
        WHEN a user applies for an offer with correct data
        THEN a 4040 status code is returned.
    """
    response = requests.request(operation, l_oppfi_offer_url, headers = g_headers, json = l_payload)
    pytest.assume(response.status_code == 404, 'actual status code was {}'.format(response.status_code))


def test_offer_noapikey(l_payload, l_oppfi_offer_url, g_headers):
    """
        GIVEN offer endpoint is up and running
        WHEN a user applies for an offer with correct data
        THEN a 403 status code is returned.
    """
    del g_headers['x-api-key']
    response = requests.post(l_oppfi_offer_url, headers = g_headers, json = l_payload)
    pytest.assume(response.status_code == 403, 'actual status code was {}'.format(response.status_code))
