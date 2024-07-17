import pytest

from src.assertions.assertions import assert_response_status
from src.testdata import TestData
from tests.customer.setup import setup_module, send_request_of_checking_email
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.regression
def test_POST_Verificar_status_code_200_cuando_se_envia_el_request_para_verificar_email(setup_module):
    payload = {
            "customerEmail": "1@gmail.com"
    }
    send_request_of_checking_email(payload)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_Verificar_el_email_cuando_esta_asociado_a_algun_customer(setup_module):
    payload = {
            "customerEmail": "1@gmail.com"
    }
    response = send_request_of_checking_email(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_Verificar_el_email_cuando_se_envia_un_website_id_0(setup_module):
    payload = {
        "customerEmail": "1@gmail.com",
        "websiteId": 0
    }
    response = send_request_of_checking_email(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_verficar_si_un_email_invalido_esta_asociado_a_algun_customer(setup_module):
    payload = {
            "customerEmail": "Email invalido"
    }
    response = send_request_of_checking_email(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response == False


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_POST_verficar_si_un_email_vacio_esta_asociado_a_algun_customer(setup_module):
    payload = {
            "customerEmail": ""
    }
    response = send_request_of_checking_email(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response == True