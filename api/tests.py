from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class AccountsTest(APITestCase):
    def setUp(self):
        # We want to go ahead and originally create a user. 
        self.test_user = User.objects.create_user('hashs', 'test@example.com')

        # URL for creating an account.
        self.create_url = reverse('account-create')

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """
        data = {
            'FirstName': 'foobar',
            'LastName': 'dshg',
            'Email': 'foobar@example.com',
            'Gender': 'male',
            'Amount': '$123',
            'Password': 'somepassword'
        }
    def get_queryset(self):
        queryset = Users.get_queryset()
        queryset = queryset # TODO
        return queryset
    
    def test_create_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 8.
        """
        data = {
                'username': 'foobar',
                'email': 'foobarbaz@example.com',
                'password': 'foo'
        }
        
    def get_queryset(self):
        queryset = Users.get_queryset()
        queryset = queryset # TODO
        return queryset

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_password(self):
        data = {
                'username': 'foobar',
                'email': 'foobarbaz@example.com',
                'password': ''
        }

    def get_queryset(self):
        queryset = Users.get_queryset()
        queryset = queryset # TODO
        return queryset
        
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

        
        response = self.client.post(self.create_url , data, format='json')

        # We want to make sure we have two users in the database..
        self.assertEqual(User.objects.count(), 2)
        # And that we're returning a 201 created code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Additionally, we want to return the username and email upon successful creation.
        self.assertEqual(response.data['FirstName'], data['FirstName'])
        self.assertEqual(response.data['LastName'], data['LastName'])
        self.assertEqual(response.data['Gender'], data['Gender'])
        self.assertEqual(response.data['Amount'], data['Amount'])
        self.assertEqual(response.data['Email'], data['Email'])
        self.assertFalse('Password' in response.data)
