from django.db import models
from django.contrib.auth.models import User
from time import time



class user(models.Model):
	fname = models.CharField(max_length = 50,default = " ")
	lname = models.CharField(max_length = 50,default = " ")
	email = models.EmailField()
	stream = models.CharField(max_length=3,default = "ECE")
	role = models.IntegerField(max_length = 1, default = 0)		# 0 ->no info, 1 ->member, 3 ->admin, 5 ->prof
	batch = models.CharField(max_length = 9, default = "Btech2014")
	rollno = models.IntegerField(max_length = 7)

