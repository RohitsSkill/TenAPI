from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from . models import courses
from . models import internships
from . makeJson import courseJson
from . makeJson import internJson

# Create your views here.
class courseList(APIView):

	def get(self,request):
		course = courses.objects.all()
		json = courseJson(course, many=True)
		return Response(json.data)

	def post(self,request):
		pass 

class internshipList(APIView):

	def get(self,request):
		internship = internships.objects.all()
		json = internJson(internship, many=True)
		return Response(json.data)

	def post(self,request):
		pass 