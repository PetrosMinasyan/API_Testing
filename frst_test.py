import json
import jsonpath
import requests
import pytest
from pprint import pprint

PostUrl = 'https://fakerestapi.azurewebsites.net/'
GetRequest = 'api/v1/Authors/1'
PostRequest = 'api/v1/Authors'
PutRequest = 'api/v1/Authors/0'
deleteRequest = 'api/v1/Authors/0'


def test_get():
    request = requests.get(PostUrl + GetRequest)
    status_code = request.status_code
    reason = request.reason
    print(f"{status_code} is {reason}")
    assert status_code == 200


def test_post():
    data = {
        "id": 0,
        "idBook": 0,
        "firstName": "string",
        "lastName": "string"
    }

    headers = {"Content-Type": "application/json"}
    EndpointURL = PostUrl + PostRequest
    response = requests.post(EndpointURL, json=data, headers=headers)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8; v=1.0"
    new_json = response.json()
    key1 = "id"
    key2 = "idBook"
    assert key1 in new_json
    assert key2 in new_json

def test_put():
    body = {
        "id": 0,
        "idBook": 0,
        "firstName": "string",
        "lastName": "string"
    }
    put_url = PostUrl + PutRequest
    response = requests.put(put_url, json=body)
    assert response.status_code == 200


def test_del():
    send_request = requests.delete(PostUrl + deleteRequest)
    st_code = send_request.status_code
    assert st_code == 200