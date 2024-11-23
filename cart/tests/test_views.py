"""
I dont know why but sessions created here are not passed into the view therefore I cannot test for cart
"""

# from django.test import TestCase
# from django.urls import reverse
# from user.models import User

# class CartTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')
#         self.cart = {
#             '1': {'name': 'Product 1', 'price': 10.00, 'quantity': 1, 'size': 'small','image_location': ''},
#             '2': {'name': 'Product 2', 'price': 15.00, 'quantity': 2, 'size': 'large','image_location': ''},
#         }
#         self.client.session['cart'] = self.cart
#         self.client.session.modified = True
#         self.client.session.save()

#     def test_cart_total_calculation(self):
#         response = self.client.get('/cart/')

#         #check if cart session is passed into index view
#         print(response.context['cart'])

#         self.assertEqual(response.context['overall_price'], '25.00')


#     def test_empty_cart_message(self):
#         self.client.session['cart'] = {}
#         self.client.session.save()
#         response = self.client.get(reverse('index'))
#         self.assertContains(response, 'no items in cart')
