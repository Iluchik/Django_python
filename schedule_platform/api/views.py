from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Category
from .serialises import CategorySerializer

class CategoryAPI(APIView):

	def get(self, req):
		categories = Category.objects.all()
		print(categories)
		serializer = CategorySerializer(categories, many=True)
		return Response(serializer.data)
	
	def post(self, req):
		category = CategorySerializer(data=req.data)
		if category.is_valid():
			category.save()
			return Response(category.data)
		
	def put(self, req):
		pass

	def delete(self, req):
		pass