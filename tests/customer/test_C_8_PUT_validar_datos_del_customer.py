import json
import pytest

from src.assertions.assertions import assert_response_status
from src.testdata import TestData
from tests.conftest import setup_data
from tests.customer.setup import send_request_of_valideting_a_customer

@pytest.mark.smoke
@pytest.mark.regression
def test_C8TC15_PUT_verificar_respuesta_200_para_validar_datos_de_customer(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "ejemplo@gmail.com",
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC16_PUT_validar_los_datos_en_customer_cuando_el_group_id_tiene_mas_de_50_digitos(setup_data):
    digitos50=12345678901234567890123456789012345678901234567890
    payload = {
      "customer": {
        "group_id":digitos50,
        "email": "ejemplo@gmail.com",
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC17_PUT_validar_los_datos_en_customer_cuando_el_email_es_correcto(setup_data):
    email="ejemplo@gmail.com"
    payload = {
      "customer": {
        "group_id":1,
        "email": email,
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == True

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC18_PUT_validar_los_datos_en_customer_cuando_dato_que_envia_a_email_no_es_correcto(setup_data):
    email="12345"
    payload = {
      "customer": {
        "group_id":1,
        "email": email,
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    # deberia ser False
    assert response["valid"] == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC19_PUT_validar_los_datos_en_customer_cuando_el_firstname_contiene_caracteres_especiales(setup_data):
    primernombre = "#$%&/()"
    payload = {
      "customer": {
        "group_id":1,
        "email": "email",
        "firstname":primernombre,
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC20_PUT_validar_los_datos_en_customer_cuando_no_se_envia_email(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == False


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC21_PUT_validar_los_datos_en_customer_cuando_se_envia_email_vacio(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "",
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == False

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC22_PUT_validar_los_datos_en_customer_cuando_se_envia_group_id_0(setup_data):
    payload = {
      "customer": {
        "group_id":0,
        "email": "sample@gmail.com",
        "firstname":"prueba",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC23_PUT_validar_los_datos_en_customer_cuando_se_envia_firstname_vacio(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "sample@gmail.com",
        "firstname":"",
        "lastname": "prueba2",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == False


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC24_PUT_validar_los_datos_en_customer_cuando_se_envia_lastname_vacio(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "sample@gmail.com",
        "firstname":"prueba1",
        "lastname": "",
        "website_id":1

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == False


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC25_PUT_validar_los_datos_en_customer_cuando_se_envia_website_id_0(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "sample@gmail.com",
        "firstname":"prueba1",
        "lastname": "prueba2",
        "website_id":0

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == True


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_C8TC25_PUT_validar_los_datos_en_customer_cuando_se_envia_website_id_nulo(setup_data):
    payload = {
      "customer": {
        "group_id":1,
        "email": "sample@gmail.com",
        "firstname":"prueba1",
        "lastname": "prueba2",
        "website_id":None

      }
    }
    response = send_request_of_valideting_a_customer(payload)
    assert_response_status(TestData.response_status_code, 200)
    assert response["valid"] == False
