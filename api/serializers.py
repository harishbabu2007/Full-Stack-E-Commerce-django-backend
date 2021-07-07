from rest_framework import serializers
from .models import Products, Cart

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Products
		fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cart
		fields = "__all__"