from app import app
from utils import get_keys_from_json
import pytest

def test_app_1():
    response = app.test_client().get('/api/posts')
    assert response.json


def test_app_2():
    response = app.test_client().get('/api/posts')
    keys = get_keys_from_json()
    for el in response.json:
        for key in keys:
            assert (bool(key in el.keys()) == True), key in el.keys()


def test_app_3():
    response = app.test_client().get('/api/posts/1')
    assert response.json


def test_app_4():
    response = app.test_client().get('/api/posts/4')
    keys = list(get_keys_from_json())
    keys.sort()
    keys_in_fact = []
    for key in response.json:
        keys_in_fact.append(key)
    assert list(keys_in_fact) == list(keys)






