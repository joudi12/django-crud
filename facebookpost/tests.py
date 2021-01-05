 
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Share

# Create your tests here.

class ShareCRUDTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'joudi',
            email = 'awamehj@gmail.com',
            password = '112233joudi'
        )

        self.share = Share.objects.create(
            title = 'game',
            author = self.user,
            body = 'every day play game it will be perfect'
        )

    def test_all_fields(self):
        response = self.client.get(reverse('details', args='1'))
        
        self.assertContains(response, 'game')
        self.assertContains(response, 'joudi')
        self.assertContains(response, 'every day play game it will be perfect') 

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_details_view(self):
        response = self.client.get(reverse('details', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        response = self.client.post(reverse('edit', args='1'), {
            'title': 'programming',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'programming')
        self.assertNotContains(response, 'game')

    def test_create_view(self):
        response = self.client.post(reverse('add'), {
            'title': 'have fun',
            'author': self.user,
            'body' :'every day smile it will make you so happy',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'have fun')
        self.assertContains(response, 'every day smile it will make you so happy')
        self.assertContains(response, 'joudi')

   
    def test_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertNotContains(response, 'programming')


    
  

  

    

    

