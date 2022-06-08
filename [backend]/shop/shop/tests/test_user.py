import pytest
import pip._vendor.requests as requests

user_endpoint = "http://localhost:8000/v1/users/"

class TestUser:
  def test_user_creation(self):
    response = requests.post(user_endpoint+'create', {
      'username': 'test',
      'email': 'test@example.com',
      'password': 'test'
    })
    print(response.json())
    assert response.json().get('status') == 'success'
  def test_user_creation_with_existing_email(self):
    response = requests.post(user_endpoint+'create', {
      'username': 'test',
      'email': 'test@example.com',
      'password': 'test'
    })
    assert response.json().get('message') == 'User with this Username already exists.'

  def test_user_login(self):
    response = requests.post(user_endpoint+'login', {
      'username': 'test',
      'password': 'test'
    })
    print(response.json())
    assert response.json().get('status') == 'success' and response.cookies.get('sessionid') is not None
  
  def test_user_login_with_invalid_username(self):
    response = requests.post(user_endpoint+'login', {
      'username': 'testinvalidusername',
      'password': 'test'
    })
    assert response.json().get('message') == 'Invalid username or password.'

  def test_user_login_with_invalid_password(self):
    response = requests.post(user_endpoint+'login', {
      'username': 'test',
      'password': 'testivalidpassword'
    })
    assert response.json().get('message') == 'Invalid username or password.'

  def test_user_login_with_invalid_username_and_password(self):
    response = requests.post(user_endpoint+'login', {
      'username': 'testinvalidusername',
      'password': 'testivalidpassword',
    })
    assert response.json().get('message') == 'Invalid username or password.'
  
  def test_user_details(self):
    sess = requests.Session()
    sess.post(user_endpoint+'login', {
      'username': 'test',
      'password': 'test'
    })
    response = sess.get(user_endpoint+'details')
    assert response.json().get('user')["username"] is not None
    
  def test_user_delete(self):
    sess = requests.Session()
    sess.post(user_endpoint+'login', {
      'username': 'test',
      'password': 'test'
    })
    response = sess.post(user_endpoint+'delete', {
      'password': 'test'
    })
    assert response.json().get('status') == 'success'
  