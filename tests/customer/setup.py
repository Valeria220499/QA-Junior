import json

import pytest
import requests

from src.enums.method import Method
from src.enums.uri import URIComplement
from src.headers.headers import header_content_type_authorization, header_authorization
from src.testdata import TestData
from tests.conftest import get_token_login
from tests.helpers.utils import Utils


@pytest.fixture(scope="function")
def setup_function():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    random_value = Utils().get_random_alphanumeric(10)
    TestData.function_response_json = send_request_of_create_a_customer(f"{random_value}@gmail.com", f"{random_value}_FN", f"{random_value}_LN")

    def teardown():
        send_request_of_remove_customer(TestData.function_response_json["id"])
    yield TestData.token
    teardown()

@pytest.fixture(scope="module")
def setup_module():
    TestData.token = get_token_login() if TestData.token is None else TestData.token
    random_value = Utils().get_random_alphanumeric(10)
    TestData.module_response_json = send_request_of_create_a_customer(f"{random_value}@gmail.com", f"{random_value}_FN", f"{random_value}_LN")

    def teardown():
        send_request_of_remove_customer(TestData.module_response_json["id"])
    yield TestData.token
    teardown()


def send_request_of_remove_customer(customer_id):
    url = f"{TestData.base_url}{URIComplement.DELETE_CUSTOMER.value.replace(URIComplement.CUSTOMER_ID_KEY_NAME.value, str(customer_id))}"

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.DELETE.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_create_a_customer(
        email: str
        , firstname: str
        , lastname: str
        , group_id=1
        , default_billing="2024-04-07 23:49:59"
        , default_shipping="2024-04-07 23:49:59"
        , created_at="2024-04-07 23:49:59"
        , updated_at="2024-04-07 23:49:59"
        , created_in="Default Store View"
        , dob="2024-04-17"
        , middlename="MN"
        , prefix="P"
        , suffix="S"
        , gender=1
        , store_id=1
        , website_id=1
        , addresses=[]
        , disable_auto_group_change=0
        , password=""
        , redirectUrl="string"
):
    TestData.old_password = "Demo123#"
    url = f"{TestData.base_url}{URIComplement.POST_CUSTOMER.value}"

    payload = json.dumps({
        "customer": {
            "group_id": group_id,
            "default_billing": default_billing,
            "default_shipping": default_shipping,
            "created_at": created_at,
            "updated_at": created_at,
            "created_in": created_in,
            "dob": dob,
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "middlename": middlename,
            "prefix": prefix,
            "suffix": suffix,
            "gender": gender,
            "store_id": store_id,
            "website_id": website_id,
            "addresses": addresses,
            "disable_auto_group_change": disable_auto_group_change
        },
        "password": (TestData.old_password if password is "" else password),
        "redirectUrl": redirectUrl
    })
    headers = header_content_type_authorization(TestData.token)
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return json.loads(response.text)


def send_request_for_assign_a_new_cart_to_a_customer(customer_id):
    url = f"{TestData.base_url}{URIComplement.POST_CART_TO_CUSTOMER.value.replace(URIComplement.CUSTOMER_ID_KEY_NAME.value, str(customer_id))}"

    payload = {}
    headers = header_authorization(TestData.token)
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)

    TestData.response_status_code = response.status_code
    return response.json()


def send_request_of_update_password_of_a_customer(customer_id, new_password, old_password):
    url = f"{TestData.base_url}{URIComplement.PUT_PASSWORD_CUSTOMER.value}".replace(
        URIComplement.CUSTOMER_ID_KEY_NAME.value, f"{customer_id}")

    params = {URIComplement.PATH_PARAMETER_CUSTOMER_ID.value: customer_id}

    payload = json.dumps({
        "currentPassword": old_password,
        "newPassword": new_password
    })

    headers = header_content_type_authorization(TestData.token)
    response = requests.request(Method.PUT.value, url, headers=headers, data=payload, params=params)
    TestData.response_status_code = response.status_code

    return response.json()

def send_request_of_valideting_a_customer(payload_dict, token=None):
    url = f"{TestData.base_url}{URIComplement.PUT_CUSTOMER.value}"

    payload = json.dumps(payload_dict)

    if token != None:
        bearer_token = token
    else:
        bearer_token = TestData.token

    headers = header_content_type_authorization(bearer_token)
    response = requests.request(Method.PUT.value, url, headers=headers, data=payload)
    TestData.response_status_code = response.status_code

    return response.json()

def send_request_of_checking_email(payload_dict, token=None):
    url = f"{TestData.base_url}{URIComplement.POST_CUSTOMER_EMAIL_AVAILABLE.value}"
    payload = json.dumps(payload_dict)

    if token != None:
        bearer_token = token
    else:
        bearer_token = TestData.token

    headers = header_content_type_authorization(bearer_token)
    response = requests.request(Method.POST.value, url, headers=headers, data=payload)
    return response.json()
