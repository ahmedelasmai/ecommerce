from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from datetime import datetime
from products.models import Products, Stock

User = get_user_model()


class ProductModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create a sample image
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x00\x01\x02',  # Minimal binary content
            content_type='image/jpeg'
        )

    def test_create_product(self):
        # Create a sample product instance
        product = Products.objects.create(
            name="Test Product",
            description="A description of the test product",
            price=19.99,
            image=self.image,
            category='t-shirt',
            user=self.user
        )
        
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.category, 't-shirt')
        self.assertEqual(product.user, self.user)
        self.assertIsNotNone(product.created_at)
        self.assertIsNotNone(product.updated_at)

    def test_product_str_representation(self):
        product = Products.objects.create(
            name="Test Product",
            description="Test description",
            price=9.99,
            category="shirt",
            user=self.user
        )
        self.assertEqual(str(product), "Test Product")

    def test_image_upload_path(self):
        product = Products.objects.create(
            name="Test Product",
            description="Test description",
            price=9.99,
            image=self.image,
            category="shirt",
            user=self.user
        )
        # Check if image path includes "images/" and the timestamped file name
        self.assertIn("images/", product.image.name)
        self.assertIn(datetime.now().strftime('%Y%m%d'), product.image.name)  # check for current date in the filename


class StockModelTest(TestCase):

    def setUp(self):
        # Create a test user and a test product
        self.user = User.objects.create_user(username='testuser', password='password')
        self.product = Products.objects.create(
            name="Test Product",
            description="Product with stock",
            price=39.99,
            category="jacket",
            user=self.user
        )

    def test_create_stock(self):
        # Create a stock entry associated with the product
        stock = Stock.objects.create(
            product=self.product,
            small=10,
            medium=20,
            large=15
        )

        self.assertEqual(stock.product, self.product)
        self.assertEqual(stock.small, 10)
        self.assertEqual(stock.medium, 20)
        self.assertEqual(stock.large, 15)

    def test_stock_str_representation(self):
        stock = Stock.objects.create(
            product=self.product,
            small=5,
            medium=10,
            large=8
        )
        self.assertEqual(str(stock), "Test Product_stock")

    def test_stock_negative_values(self):
        # Ensure negative stock values are not allowed
        with self.assertRaises(ValueError):
            Stock.objects.create(
                product=self.product,
                small=-1,  # Invalid
                medium=0,
                large=10
            )

    def test_delete_product_cascades_stock(self):
        # Verify that deleting a product also deletes its stock
        stock = Stock.objects.create(
            product=self.product,
            small=5,
            medium=10,
            large=8
        )
        self.product.delete()
        
        # Stock should no longer exist
        with self.assertRaises(Stock.DoesNotExist):
            Stock.objects.get(id=stock.id)


class ProductStockIntegrationTest(TestCase):
    def setUp(self):
        # Create user, product, and stock to test the association
        self.user = User.objects.create_user(username='testuser', password='password')
        self.product = Products.objects.create(
            name="Integrated Product",
            description="Product with stock integration",
            price=59.99,
            category="jeans",
            user=self.user
        )
        self.stock = Stock.objects.create(
            product=self.product,
            small=5,
            medium=15,
            large=10
        )

    def test_product_with_stock(self):
        # Test the linked relationship between product and stock
        self.assertEqual(self.stock.product, self.product)
        self.assertEqual(self.product.stock_set.count(), 1)
        self.assertEqual(self.product.stock_set.first(), self.stock)
