from http import HTTPStatus
from fastapi.testclient import TestClient
from fastzero.app import app



def test_read_root_dev_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (organização)`
    response = client.get("/") # Act (Ação)

    assert response.status_code == HTTPStatus.OK # Assert
    assert response.json() == {'message': 'Hello World'} # Asser

