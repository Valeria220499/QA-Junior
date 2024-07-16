import json

import pytest

from src.enums.method import Method
from src.enums.static_data import StaticData
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from src.testdata import TestData
from tests.conftest import get_token_login



@pytest.fixture(scope="module")
def setup_module_inventory_stocks():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    TestData.module_response_json_stocks = None
    TestData.module_response_json_stocks = send_request_of_create_a_stock(StaticData.stock_id.value,
                                                                        StaticData.name.value,
                                                                        StaticData.extension_attributes.value)

    def teardown():
        teardown_send_request_of_remove_customer(TestData.module_response_json_stocks)
    yield TestData.token
    teardown()


def send_request_of_create_a_stock(stock_id=None, name=None, extension_attributes=None, dato_extra=None):
    TestData.response_status_code = None
    url = f"{TestData.base_url}{URIComplement.POST_INVENTORY_STOCKS.value}"
    stock_key = "stock"
    payload = {stock_key:{}}
    if stock_id is not None:
        payload[stock_key]["stock_id"] = stock_id
    if name is not None:
        payload[stock_key]["name"] = name
    if extension_attributes is not None:
        payload[stock_key]["extension_attributes"] = extension_attributes
    if dato_extra is not None:
        payload[stock_key]["dato_extra"] = dato_extra
    headers = header_content_type_authorization(TestData.token)
    response = TestData.request_client(Method.POST.value, url, headers, json.dumps(payload)).run()

    TestData.response_status_code = response.status_code
    return json.loads(response.text)


def teardown_send_request_of_remove_customer(response):
    if not isinstance(response, int):
        return
    url = f"{TestData.base_url}{URIComplement.POST_INVENTORY_STOCKS.value}/{response}"
    headers = header_content_type_authorization(TestData.token)
    TestData.request_client(Method.DELETE.value, url, headers).run()
