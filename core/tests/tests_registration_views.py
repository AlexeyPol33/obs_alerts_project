import pytest
import time
from django.core import mail
from rest_framework.test import APIClient
from django.contrib.auth.hashers import check_password
from django.urls import reverse
from django.db import transaction
from django.test import TransactionTestCase
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from user_cabinet.models import User


URL = '/user/'

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def correct_user_data():
    data = []
    for i in range(10):
        data.append({
        "username": f'username{i}',
        "password": f'password{i}',
        "email": f'test{i}@email.com'})
    return data


@pytest.fixture
def incorrect_user_data():
    data0 ={
        "username": '',
        "password": 'password',
        "email": 'test@email.com'}
    data1 ={
        "username": 'username',
        "password": '',
        "email": 'test@email.com'}
    data2 ={
        "username": 'username',
        "password": 'password',
        "email": ''}
    return [data0,data1,data2]



@pytest.mark.django_db
def test_connection(api_client: APIClient):

    response = api_client.get('')
    assert response.status_code == 200

@pytest.mark.django_db
def test_correct_registration(api_client: APIClient, correct_user_data: list):

    for user in correct_user_data:
        response = api_client.post(URL,user)
        user_obj = User.objects.filter(username=user['username']).first()
        assert response.status_code == 201
        assert user_obj.username == user['username']
        assert check_password(user['password'], user_obj.password)
        assert user_obj.email == user['email']

@pytest.mark.django_db
def test_user_permissions(api_client: APIClient, correct_user_data: list):
    for user in correct_user_data:
        response = api_client.post(URL,user)
        assert response.status_code == 201
        token = api_client.post('/api/token/',user)
        assert token.status_code == 200
        response = api_client.get(URL)
        response = api_client.put(URL)
        response = api_client.patch(URL)
        
    pass

