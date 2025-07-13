# products/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product
from users.models import UserProfile
from decimal import Decimal  # Add this import

class ProductModelTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', password='password')
        UserProfile.objects.create(user=self.admin_user, role='admin')
        self.product = Product.objects.create(
            name='Test Product',
            description='A test product',
            price=19.99,
            created_by=self.admin_user
        )

    def test_product_creation(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.description, 'A test product')
        self.assertEqual(product.price, Decimal('19.99'))  # Change 19.99 to Decimal('19.99')
        self.assertEqual(product.created_by, self.admin_user)