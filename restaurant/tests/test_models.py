from django.test import TestCase
from restaurant.models import Booking, Menu
from datetime import date


class BookingModelTests(TestCase):
    def test_booking_str(self):
        b = Booking.objects.create(first_name='Alice', reservation_date=date.today(), reservation_slot=1)
        self.assertEqual(str(b), 'Alice')

    def test_default_slot(self):
        b = Booking.objects.create(first_name='Bob', reservation_date=date.today())
        # default reservation_slot defined in model is 10
        self.assertEqual(b.reservation_slot, 10)


class MenuModelTests(TestCase):
    def test_menu_str_and_fields(self):
        m = Menu.objects.create(name='Margherita', price=10, menu_item_description='Cheesy pizza')
        self.assertEqual(str(m), 'Margherita')
        self.assertEqual(m.price, 10)
        self.assertIn('Cheesy', m.menu_item_description)
