import json
from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Booking, Menu
from datetime import date


class SimpleViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_and_about(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        res = self.client.get(reverse('about'))
        self.assertEqual(res.status_code, 200)

    def test_menu_and_menu_item(self):
        # create a menu item
        m = Menu.objects.create(name='Pasta', price=12, menu_item_description='Tasty')
        res = self.client.get(reverse('menu'))
        self.assertEqual(res.status_code, 200)

        # display specific menu item
        res = self.client.get(reverse('menu_item', kwargs={'pk': m.pk}))
        self.assertEqual(res.status_code, 200)
        # view passes the menu_item in context
        self.assertIn('menu_item', res.context)
        self.assertEqual(res.context['menu_item'].pk, m.pk)


class BookingsViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('bookings')

    def test_post_create_booking_and_get(self):
        payload = {
            'first_name': 'Charlie',
            'reservation_date': str(date.today()),
            'reservation_slot': 3,
        }
        # POST JSON to create booking
        res = self.client.post(self.url, data=json.dumps(payload), content_type='application/json')
        # view returns 200 on success
        self.assertEqual(res.status_code, 200)
        # booking should exist in DB
        exists = Booking.objects.filter(first_name='Charlie', reservation_slot=3, reservation_date=payload['reservation_date']).exists()
        self.assertTrue(exists)

        # GET bookings for that date
        res = self.client.get(self.url, {'date': payload['reservation_date']})
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.content)
        # should be a list of serialized booking objects
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)

    def test_duplicate_slot_returns_error(self):
        payload = {
            'first_name': 'Dana',
            'reservation_date': str(date.today()),
            'reservation_slot': 5,
        }
        # create first booking
        res1 = self.client.post(self.url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res1.status_code, 200)

        # try to create duplicate
        res2 = self.client.post(self.url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res2.status_code, 200)
        # duplicate returns an error JSON string containing 'error'
        self.assertIn(b'error', res2.content)
