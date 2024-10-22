import requests
from requests.auth import HTTPBasicAuth

url = "http://host.com"
username = "username"
password = "password"


def test_crud_user():
    ID = 0
    Hash = None
    IsSystemUser = False
    FirstName = "John"
    LastName = "Dou"
    FullName = None
    Organization = "Funny Duck"
    Department = "IT"
    JobPosition = "QA Engeneer"
    HiredDate = "2023-07-02T00:00:00+03:00"
    response = requests.post(url + '/api/users',
                             json={"ID": ID,
                                    "Hash": Hash,
                                    "IsSystemUser": IsSystemUser,
                                    "FirstName": FirstName,
                                    "LastName": LastName,
                                    "FullName": FullName,
                                    "Organization": Organization,
                                    "Department": Department,
                                    "JobPosition": JobPosition,
                                    "HiredDate": HiredDate},
                             auth=HTTPBasicAuth(username, password))
    print(response)
    id = response

    response = requests.get(url + '/api/users/' + id)
    body = response.json()
    assert body.FirstName == FirstName

    JobPositionNew = "Lead QA"
    response = requests.put(url + '/api/users/' + id,
                            json={"ID": ID,
                                  "Hash": Hash,
                                  "IsSystemUser": IsSystemUser,
                                  "FirstName": FirstName,
                                  "LastName": LastName,
                                  "FullName": FullName,
                                  "Organization": Organization,
                                  "Department": Department,
                                  "JobPosition": JobPositionNew,
                                  "HiredDate": HiredDate},
                            auth=HTTPBasicAuth(username, password))

    response = requests.get(url + '/api/users/' + id)
    body = response.json()
    assert body.JobPosition == JobPositionNew

    response = requests.delete(url + '/api/users/',
                               json={'id':id},
                               auth=HTTPBasicAuth(username, password))

    response = requests.get(url + '/api/users/' + id)
    assert response.status_code == 404



