import requests
from requests import Response
from pytest_voluptuous import S
from schemas.schemas import single_user, update_user, login_user, create_user, register_user


def test_get_single_user_status_code(reqres):
    response = reqres.get('api/users/2')

    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_post_create_user(reqres):
    created_user = reqres.post('api/users',
                                           json=
                                           {
                                               "name": "test_name",
                                               "job": "QA"
                                           }
                                           )

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "test_name"
    assert created_user.json()["job"] == "QA"


def test_put_update_user(reqres):
    updated_user = reqres.put('api/users/2',
                                          json=
                                          {
                                              "name": "test_name1",
                                              "job": "Writer"
                                          }
                                          )

    assert updated_user.status_code == 200
    assert S(update_user) == updated_user.json()
    assert updated_user.json()["name"] == "test_name1"
    assert updated_user.json()["job"] == "Writer"


def test_post_register_user(reqres):
    registered_user: Response = reqres.post('api/register',
                                              json=
                                              {
                                                  "email": "eve.holt@reqres.in",
                                                  "password": "123321"
                                              }
                                              )

    assert registered_user.status_code == 200
    assert S(register_user) == registered_user.json()
    assert registered_user.json()["token"] is not None
    assert len(registered_user.json()["token"]) == 17


def test_post_login_user(reqres):
    logined_user: Response = reqres.post('api/login',
                                           json=
                                           {
                                               "email": "eve.holt@reqres.in",
                                               "password": "123321"
                                           }
                                           )

    assert logined_user.status_code == 200
    assert S(login_user) == logined_user.json()
    assert logined_user.json()["token"] is not None
    assert len(logined_user.json()["token"]) == 17
