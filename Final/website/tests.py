import unittest
from .models import User, website_products
from django.db.utils import IntegrityError
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import searchProduct

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='hagit123',
            first_name='Hagit',
            last_name='Tubul',
            email='hagit4@gmail.com',
            location='Ashdod',
            comp_num=12345
        )

    def test_user_creation(self):    # Test unit to check user creation (not AI) - made by Aviram
        self.assertEqual(self.user.username, 'hagit123')
        self.assertEqual(self.user.first_name, 'Hagit')
        self.assertEqual(self.user.last_name, 'Tubul')
        self.assertEqual(self.user.email, 'hagit4@gmail.com')
        self.assertFalse(self.user.user_type)  
        self.assertEqual(self.user.location, 'Ashdod')
        self.assertEqual(self.user.comp_num, 12345)

    def test_user_unique_email(self):    # AI Unit Testing - GEMINI
        with self.assertRaises(Exception):
            # Attempt to create a user with the same email
            User.objects.create(
                username='test_user_2',
                first_name='Jane',
                last_name='Doe',
                email='hagit4@gmail.com',  # This email should already exist
                location='Test City',
                comp_num=54321
            )
    def test_user_type_choices(self):    # AI Unit Testing - GEMINI
        # Test user_type field choices
        self.assertTrue(self.user.USER_TYPE_CHOICES, (
            (False, 'Private'),
            (True, 'Corporation')
        ))
    
    def test_user_comp_num_blank(self):    # AI Unit Testing - GEMINI
        # Test comp_num field can be blank
        user_no_comp_num = User.objects.create(
            username='test_user_no_comp_num',
            first_name='Jane',
            last_name='Doe',
            email='no_comp_num@example.com',
            location='Test City'
        )
        self.assertIsNone(user_no_comp_num.comp_num)

class WebsiteProductsModelTests(unittest.TestCase):
    # my test unit
    def test_product_creation(self):   # Test unit to check that a product was created successfully - made by Noam
        product = website_products.objects.create(
            product_name='Test Product',
            Product_type=True,
            value=50,
            bin_type='Type A'
        )

        self.assertIsNotNone(product)
        self.assertEqual(product.product_name, 'Test Product')
        self.assertTrue(product.Product_type)
        self.assertEqual(product.value, 50)
        self.assertEqual(product.bin_type, 'Type A')

    def test_product_str_method(self):  # Made by AI - Microsoft Copilot
        # Create a product instance
        product = website_products(product_name='Test Product', bin_type='Type A')

        # Check the __str__ method
        self.assertEqual(str(product), 'Test Product, Type A')

    def test_product_type_default(self):   # Made by AI - Microsoft Copilot
        # Create a product without specifying Product_type (should default to False)
        product = website_products.objects.create(
            product_name='Another Product',
            value=100,
            bin_type='Type B'
        )

        self.assertFalse(product.Product_type)

    def test_invalid_value_raises_error(self): # Made by AI - Microsoft Copilot
    # Attempt to create a product with a negative value (should raise an IntegrityError)
        with self.assertRaises(IntegrityError):
            try:
                website_products.objects.create(
                    product_name='Invalid Product',
                    Product_type=True,
                    value=-10,  # Negative value
                    bin_type='Type C'
                )
            except IntegrityError as e:
                # Check if the IntegrityError message contains the expected substring
                self.assertTrue('CHECK constraint failed: value' in str(e))
                raise



if __name__ == '__main__':
    unittest.main()