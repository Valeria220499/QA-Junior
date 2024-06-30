import pytest
import requests
import jsonschema
from src.singleton import Singleton


# CG-06-TC1: [GET] Verificar obtención exitosa de un grupo de clientes por ID
@pytest.mark.smoke
def test_CG_06_TC1_GET_verificar_obtencion_exitosa_de_un_grupo_de_clientes_por_id(get_token_login):
    group_id = 1  # ID válido de un grupo de clientes existente

    token = get_token_login
    url = f"{Singleton.get_base_url()}/rest/default/V1/customerGroups/{group_id}"

    headers = {
        'Authorization': f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)
    response_data = response.json()

    assert response.status_code == 200
    assert "id" in response_data
    assert response_data["id"] == group_id
    assert "code" in response_data
    assert "tax_class_id" in response_data
    assert "tax_class_name" in response_data
def test_schema_customer_group(get_token_login):
    token = get_token_login
    response_data = get_body_of_obtain_customer_group_by_id(1, token)
    schema = Singleton.read_schema_json_file('get_customer_group.json')
    try:
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f'JSON schema dont match {err}')