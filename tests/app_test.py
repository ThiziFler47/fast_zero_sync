from http import HTTPStatus

from fastapi.testclient import TestClient


def test_read_root_dev_retornar_ok_e_ola_mundo(client: TestClient):
    # 1 Arrange (organização)`
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello World'}  # Asser


def test_create_user(client: TestClient):
    response = client.post(
        url='/users/',
        json={
            'username': 'testusername',
            'email': 'test@email.com',
            'password': 'passowrd',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@email.com',
        'id': 0,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@email.com',
                'id': 0,
            }
        ]
    }


def test_update_users(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'testupdateusername',
            'email': 'test@email.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testupdateusername',
        'email': 'test@email.com',
        'id': 0,
    }

    response = client.put(
        '/users/1',
        json={
            'username': 'testupdateusername',
            'email': 'test@email.com',
            'password': 'test1234',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User Not Found'}


def test_delete_user(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User Deleted!'}

    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User Not Found'}
