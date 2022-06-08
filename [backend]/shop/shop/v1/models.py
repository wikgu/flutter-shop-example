from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
  name = models.CharField(max_length=30)
  description = models.TextField()
  price = models.FloatField()
  image_url = models.URLField(default='https://cdn.onlinewebfonts.com/svg/img_231353.png')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

  def get_price(self):
    return self.price

class CartItem(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.user_id) + " " + str(self.product_id) + " " + str(self.quantity)

  def get_quantity(self):
    return self.quantity

  def get_product_id(self):
    return self.product_id

  def get_user_id(self):
    return self.user_id

  def get_total_price(self):
    return self.product_id.price * self.quantity