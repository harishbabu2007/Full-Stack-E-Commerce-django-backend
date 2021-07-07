from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length=200)
	price = models.IntegerField()
	url_slug_pk = models.SlugField(max_length=255, default=name, primary_key=True)
	url_slug = models.SlugField(max_length=255, default=name)
	category = models.CharField(max_length=200, default="General")
	description = models.CharField(max_length=500)
	picture_url = models.URLField(max_length=500)
	company = models.CharField(max_length=200)
	purchased_amount = models.IntegerField(default=0)

	def __str__(self):
		return self.name


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_user")
	product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="cart_product")