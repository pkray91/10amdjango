from django.db import models

class Employee(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField()
	image = models.ImageField(default="")
	mobile = models.BigIntegerField()
	salary = models.IntegerField()

	class Meta:
		db_table = 'employee'

