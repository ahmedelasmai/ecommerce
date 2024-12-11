from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.urls import reverse

from products.models import Products, Stock
from products.forms import ProductForm, ProductModelForm, StockModelForm

User = get_user_model()


class ProductStockIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=b"\x00\x01\x02",
            content_type="image/jpeg",
        )
        # models
        self.product = Products.objects.create(
            name="Integrated Product",
            description="Product with stock integration",
            price=59.99,
            image=self.image,
            category="jeans",
            user=self.user,
        )
        self.stock = Stock.objects.create(
            product=self.product, small=10, medium=10, large=10
        )

    # test you cannot add product to cart if not enough in stock
    def test_product_with_not_enough_stock(self):
        url = reverse("product", kwargs={"pk": 1})
        form_data = {"size": "small", "quantity": 12}

        self.client.post(url, data=form_data)


class ProductFormTest(TestCase):
    def test_valid_product_form(self):
        form_data = {"size": "medium", "quantity": 2}
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["size"], "medium")
        self.assertEqual(form.cleaned_data["quantity"], 2)

    def test_invalid_product_form(self):
        # Test with invalid data
        form_data = {
            "size": "",
            "quantity": -1,
        }
        form = ProductForm(data=form_data)
        self.assertIn("size", form.errors)
        self.assertIn("quantity", form.errors)


class ProductModelFormTest(TestCase):
    def test_invalid_product_model_form(self):
        form_data = {
            "name": "",
            "price": -5.00,
            "description": "A great product.",
            "category": "Test Category",
            "image": None,
        }

        form = ProductModelForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("price", form.errors)


class StockModelFormTest(TestCase):
    def test_valid_stock_model_form(self):
        form_data = {"small": 10, "medium": 5, "large": 2}

        form = StockModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_stock_model_form(self):
        form_data = {"small": -1, "medium": 5, "large": 2}

        form = StockModelForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("small", form.errors)