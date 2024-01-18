import configuration
import requests
import data
def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.create_body,
                         headers=data.headers)
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                         params={"t": track})
def test_order():
    response = post_create_order()
    track = response.json()["track"]
    response = get_order(track)

    assert response.status_code == 200
# Анастасия Глаголева, 12-я когорта - Финальный проект. Инженер по тестированию плюс.
