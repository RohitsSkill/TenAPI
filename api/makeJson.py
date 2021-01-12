from rest_framework import serializers
from . models import courses
from . models import internships

class courseJson(serializers.ModelSerializer):

	class Meta:
		model = courses
		fields = '__all__'

class internJson(serializers.ModelSerializer):

	class Meta:
		model = internships
		fields = '__all__'
