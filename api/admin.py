from django.contrib import admin
from . models import courses
from . models import internships

admin.site.register(courses)
admin.site.register(internships)
# Register your models here.
# class course :

# 	get():
# 		return couseJson.meta