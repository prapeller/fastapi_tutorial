from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

x_token = 'keycloak'


def test_users_list():
    resp = client.get('/users', headers={'X-Token': x_token})
    assert resp.status_code == 200


def test_users_list_bad_token():
    resp = client.get('/users', headers={'X-Token': 'bad_token'})
    assert resp.status_code == 400


def test_users_create():
    resp = client.post('/users', headers={'X-Token': x_token},
                       json={'email': 'pavelmirosh@gmail.com',
                             'password': 'testpassword'})
    assert resp.status_code == 307
