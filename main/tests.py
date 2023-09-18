from django.test import TestCase, Client
from .models import Item


class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Blue Potion', amount=5, description='Potion for test purpose only',
                            effect='Give your test result', value=100)

    def test_name_label(self):
        item = Item.objects.get(id=1)
        expected_output = item._meta.get_field('name').verbose_name
        self.assertEqual(expected_output, 'name')

    def test_amount_label(self):
        item = Item.objects.get(id=1)
        expected_output = item._meta.get_field('amount').verbose_name
        self.assertEqual(expected_output, 'amount')

    def test_description_label(self):
        item = Item.objects.get(id=1)
        expected_output = item._meta.get_field('description').verbose_name
        self.assertEqual(expected_output, 'description')

    def test_effect_label(self):
        item = Item.objects.get(id=1)
        expected_output = item._meta.get_field('effect').verbose_name
        self.assertEqual(expected_output, 'effect')

    def test_value_label(self):
        item = Item.objects.get(id=1)
        expected_output = item._meta.get_field('value').verbose_name
        self.assertEqual(expected_output, 'value')

    def test_name_max_length(self):
        item = Item.objects.get(id=1)
        expected_length = item._meta.get_field('name').max_length
        self.assertEqual(expected_length, 100)
