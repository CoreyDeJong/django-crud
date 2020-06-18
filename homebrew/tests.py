from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Beers


class SnackTests(TestCase):

    def setUp(self):
        # will create a new user everytime each test is run
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        # will create an entry into the test database
        self.homebrew = Beers.objects.create(
            name='ipa',
            description='refreshing',
            brewery=self.user,
        )

    def test_string_representation(self):
        brew = Beers(name='Stout')
        self.assertEqual(str(brew), brew.name)

    def test_beer_content(self):
        self.assertEqual(f'{self.homebrew.name}', 'ipa')
        self.assertEqual(f'{self.homebrew.brewery}', 'tester')
        self.assertEqual(f'{self.homebrew.description}', 'refreshing')

    def test_beer_list_view(self):
        response = self.client.get(reverse('beer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ipa')
        self.assertTemplateUsed(response, 'beer_list.html')

    def test_beer_detail_view(self):
        response = self.client.get('/beer/1/')
        no_response = self.client.get('/beer/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'refreshing')
        self.assertTemplateUsed(response, 'beer_detail.html')


    def test_beer_create_view(self):
        response = self.client.post(reverse('beer_create'), {
            'name': 'Bud lite',
            'description': 'Low carb',
            'brewery': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bud lite')
        self.assertContains(response, 'Low carb')


    # def test_beer_update_view(self):
    #     response = self.client.post(reverse('beer_update',args='1'), {
    #         'name': 'Updated name',
    #         'description': 'Updated description',
    #     })
    #     self.assertEqual(response.status_code, 302)

    def test_beer_delete_view(self):
        response = self.client.get(reverse('beer_delete',args='1'))
        self.assertEqual(response.status_code, 200)

    def test_beer_update_view_redirect(self):
        response = self.client.post(reverse('beer_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Updated name')

        self.assertTemplateUsed('beer_detail.html')
