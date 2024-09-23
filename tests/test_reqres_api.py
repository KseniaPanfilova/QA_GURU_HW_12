import json
from jsonschema import validate
import requests

url = 'https://reqres.in'


def test_create_new_user_response_status_code():
    response = requests.post(url + '/api/users',
                             json={'name': 'morpheus', 'job': 'Zion president'})
    assert response.status_code == 201


def test_update_user_info_response_status_code():
    response = requests.put(url + '/api/users/2',
                            json={'name': 'morpheus', 'job': 'Zion president'})
    assert response.status_code == 200


def test_delete_user_response_status_code():
    response = requests.delete(url + '/api/users/2')
    assert response.status_code == 204


def test_unsuccessful_registration_response_status_code():
    response = requests.post(url + '/api/register',
                             json={'email': 'sydney@fife'})
    assert response.status_code == 400


def test_user_not_found_response_status_code():
    response = requests.get(url + '/api/users/23')
    assert response.status_code == 404


def login_user(email, password):
    response = requests.post(url + '/api/login',
                             json={'email': email, 'password': password})
    return response


def test_validation_login_information():
    assert login_user('eve.holt@reqres.in', 'cityslicka').status_code == 200
    assert login_user('', 'cityslicka').status_code == 400
    assert login_user('eve.holt@reqres.in', '').status_code == 400


def test_create_new_user_response_schema():
    response = requests.post(url + '/api/users',
                             json={'name': 'morpheus', 'job': 'Zion president'})
    body = response.json()
    with open('.\\schemas\\create_user.json') as file:
        validate(body, schema=json.loads(file.read()))


def test_login_successful_response_schema():
    response = requests.post(url + '/api/login',
                             json={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
    body = response.json()
    with open('.\\schemas\\login_successful.json') as file:
        validate(body, schema=json.loads(file.read()))


def test_get_users_list_response_schema():
    response = requests.get(url + '/api/users',
                            params={'page': 2})
    body = response.json()
    with open('.\\schemas\\users_list.json') as file:
        validate(body, schema=json.loads(file.read()))


def test_get_user_response_schema():
    response = requests.get(url + '/api/users/2')
    body = response.json()
    with open('.\\schemas\\user_info.json') as file:
        validate(body, schema=json.loads(file.read()))


def test_create_user_response_has_information_from_request():
    name = 'Neo'
    job = 'The One'
    response = requests.post(url + '/api/users',
                             json={'name': name, 'job': job})
    body = response.json()
    assert body.get('name') == name
    assert body.get('job') == job
