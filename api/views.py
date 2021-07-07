from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products, Cart
from .serializers import ProductsSerializer, CartSerializer
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import CharField
from django.db.models.functions import Lower

# Create your views here.
@api_view(["GET"])
def check_is_auth(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		if request.user.is_authenticated:
			return Response({"auth": True})

		return Response({"auth": False})
	return Response({"message": "auth error"})


@api_view(["GET"])
def list_products(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})
		
	if request.GET["key"] == "no2$gold":
		data = Products.objects.all()
		res = ProductsSerializer(data, many=True)
		return Response(res.data)
	return Response({"message": "auth error"})


@api_view(["GET"])
def get_product_by_slug(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		data = Products.objects.filter(url_slug=request.GET["slug"])
		res = ProductsSerializer(data, many=True)
		return Response(res.data)

	return Response({"message": "auth error"})


@api_view(["GET"])
def get_products_by_category(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		data = Products.objects.filter(category=request.GET["query"])
		res = ProductsSerializer(data, many=True)
		return Response(res.data)

	return Response({"message": "auth error"})


@login_required
@api_view(["GET"])
def add_product_cart(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		product = Products.objects.get(url_slug=request.GET["product_pk"])
		c = Cart(product=product, user=request.user)
		c.save()

		return Response({"message": "saved successfully"})

	return Response({"message": "auth error"})


@login_required
@api_view(["GET"])
def get_cart_products(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		cart = Cart.objects.filter(user__email=request.user.email)

		products = []
		ids = []
		rv_products = []

		for i in range(len(cart)):
			products.append(cart[i].product)
			ids.append(cart[i].id)

		for i in range(len(products)):
			rv_products.append(
				{
					"id": ids[i],
					"name": products[i].name,
					"price": products[i].price,
					"url_slug": products[i].url_slug,
					"category": products[i].category,
					"picture_url": products[i].picture_url,
					"company": products[i].company,
				}
			)


		return Response(rv_products)

	return Response({"message": "auth error"})


@login_required
@api_view(["GET"])
def delete_item_cart(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})


	if request.GET["key"] == "no2$gold":
		cart = Cart.objects.get(id=request.GET["id"])
		cart.delete()
		return Response({"message": "deleted successfully"})

	return Response({"message": "auth error"})

@login_required
@api_view(["GET"])
def get_cart_price(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		cart = Cart.objects.filter(user__email=request.user.email)

		products = []
		price = 0

		for i in range(len(cart)):
			products.append(cart[i].product)

		for i in range(len(products)):
			price += int(products[i].price)

		print(price)

		return Response({"price": price})

	return Response({"message": "auth error"})


@login_required
@api_view(["GET"])
def purchase_items(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		cart = Cart.objects.filter(user__email=request.user.email)

		products = []

		for i in range(len(cart)):
			products.append(cart[i].product)

		for i in range(len(products)):			
			pro = products[i]

			pur = pro.purchased_amount
			
			pro.purchased_amount = pur + 1
			pro.save()
			print(pro.purchased_amount)



		cart.delete()

		return Response({"task": "done"})

	return Response({"message": "auth error"})


@api_view(["GET"])
def search_products(request):
	try:
		print(request.GET["key"])
	except:
		return Response({"message": "auth error"})

	if request.GET["key"] == "no2$gold":
		query = request.GET["query"]
		lookup = (
			Q(name__icontains=query) |
			Q(category__icontains=query) |
			Q(company__icontains=query)
		)

		data = Products.objects.filter(lookup)
		res = ProductsSerializer(data, many=True)
		return Response(res.data)


	return Response({"message": "auth error"})
