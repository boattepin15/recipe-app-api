from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_USER = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    """ Crate and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_create_user_succ(self,):
        """ Test createing a user is successfull"""
        payload = {
            "email":'test@gmail.com',
            'password':'test12345',
            'name':"test name"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_with_email_exists_error(self):
        """ Test Error retured if user with exists"""
        payload = {
            "email":'test@gmail.com',
            'password':'test12345',
            'name':"test name"
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_too_shrot_error(self):
        """ Test an error is return if password less than 5 char"""
        payload = {
            "email":'test@gmail.com',
            'password':'test',
            'name':"test name"
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
            ).exists()
        self.assertFalse(user_exists)
    
    def test_create_token_for_user(self):
        """ Test generate toekn for valid """
        user_deails = {
            "name":'Test Name',
            "email":'test@gmail.com',
            "password":'test-user-passwrod12345'
        }
        create_user(**user_deails)
        payload = {
            'email':user_deails['email'],
            'password':user_deails['password']
        }
        res = self.client.post(TOKEN_USER, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_create_token_bad_credentials(self):
        """ Test return error if credentials invalid."""
        create_user(
            email= "test@gmail.com",
            password = 'goodtest'
        )
        payload = {
            'email':'test@gmail.com',
            'password':'badpass'
        }
        res = self.client.post(TOKEN_USER, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_token_blank_password(self):
        """ Test posting a blank password return an error"""
        payload = {
            "email":'test@gmail.com',
            "password": ""
        }
        res = self.client.post(TOKEN_USER, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_retrueve_user_unauthorized(self):
        """ Test authentication is requrired for users."""
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateUserApiTests(TestCase):
    """ TEst API requst that required authentication"""
    def setUp(self):
        self.user = create_user(
            email='test@gmail.com',
            password='test12345',
            name='Test Name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_retrieve_profile_seuccess(self):
        """ Test retrieving profile for logged in user"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data,{
            'name':self.user.name,
            'email':self.user.email,
        })
    
    def test_post_me_not_allowed(self):
        """ Test post is not allowed for me endpoint"""
        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """ Test updating the user profile for the authenticated user"""
        payload = {
            'name':'Update Name',
            'password':'Update Password'
        }
        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)