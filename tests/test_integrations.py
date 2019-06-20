import os
import pytest
from app import app
from flask import url_for


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        pass
    yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data

def test_listpostuser(client):
    rv = client.get('/list_all_post/blackshane/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data

def test_newpost(client):
    rv = client.get('/newpost/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data

def test_(client):
    rv = client.get('/editpost/1/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data

def test_(client):
    rv = client.get('/newuser/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data

def test_(client):
    rv = client.get('/login/')
    assert rv.status_code == 200
    assert b'Microlly' in rv.data
