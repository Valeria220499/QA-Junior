import random

import pytest

from src.assertions.assertions import assert_response_status, assert_equals
from src.testdata import TestData
from tests.inventory_stocks.setup import setup_module_inventory_stocks, send_request_of_create_a_stock
from tests.conftest import setup_data


@pytest.mark.smoke
@pytest.mark.regression
def test_CS1TC1_POST_Crear_stock_con_datos_validos(setup_module_inventory_stocks):
    send_request_of_create_a_stock(stock_id=1000, name=f"neyva{random.randint(1000, 2000)}")
    assert_response_status(TestData.response_status_code, 200)


@pytest.mark.smoke
@pytest.mark.regression
def test_CS1TC2_POST_Crear_stock_sin_nombre(setup_module_inventory_stocks):
    send_request_of_create_a_stock(stock_id=1)
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CS1TC3_POST_Crear_stock_con_nombre_vacio(setup_module_inventory_stocks):
    send_request_of_create_a_stock(stock_id=1, name="")
    assert_response_status(TestData.response_status_code, 400)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CS1TC4_POST_Crear_stock_con_nombre_duplicado(setup_module_inventory_stocks):
    send_request_of_create_a_stock(name="neyva")
    response = send_request_of_create_a_stock(name="neyva")
    assert_response_status(TestData.response_status_code, 400)
    assert_equals(response["message"], "Could not save Stock")


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CS1TC5_POST_Crear_stock_con_un_dato_extra_en_payload(setup_module_inventory_stocks):
    send_request_of_create_a_stock(stock_id=10, name="Nombre", dato_extra="Apellido")
    assert_response_status(TestData.response_status_code, 500)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CS1TC6_POST_Crear_stock_con_stock_id_y_nombre(setup_module_inventory_stocks):
    random_number = random.randint(1000,2000)
    response = send_request_of_create_a_stock(stock_id=1000, name=f"neyva{random_number}")
    assert_response_status(TestData.response_status_code, 200)
    assert response == 1000


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_CS1TC7_POST_Crear_stock_con_id_nombre_y_extension_attributes_vacio(setup_module_inventory_stocks):
    random_number = random.randint(1000,2000)
    extension_attributes = {}
    response = send_request_of_create_a_stock(stock_id=1000, name=f"neyva{random_number}", extension_attributes=extension_attributes)
    assert_response_status(TestData.response_status_code, 200)
    assert response == 1000