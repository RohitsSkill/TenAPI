from django.db import models

# Create your models here.
class courses(models.Model):
	name = models.CharField(max_length = 30)
	teacher = models.CharField(max_length = 20)
	startDate = models.DateField()
	endDate = models.DateField()
	fees = models.IntegerField()

	def __str__(self):
		return self.name

class internships(models.Model):
	name = models.CharField(max_length = 30)
	hr = models.CharField(max_length = 20)
	startDate = models.DateField()
	endDate = models.DateField()
	stipend = models.IntegerField()

	def __str__(self):
		return self.name