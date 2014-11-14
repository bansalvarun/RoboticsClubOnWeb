from django.db import models
from django.contrib.auth.models import User
from time import time



class members(models.Model):
	fname = models.CharField(max_length = 50,default = " ")
	lname = models.CharField(max_length = 50,default = " ")
	email = models.EmailField()
	stream = models.CharField(max_length=3,default = "ECE")
	role = models.IntegerField(max_length = 1, default = 0)		# 0 ->no info, 1 ->member, 3 ->admin, 5 ->prof
	batch = models.CharField(max_length = 9, default = "Btech2014")
	rollno = models.IntegerField(max_length = 7)

class post(models.Model):
	title = models.CharField(max_length = 50)
	text = models.TextField(max_length = 200)
	author = models.ForeignKey(members, null=True, blank=True)

class comment(models.Model):
	text = models.CharField(max_length = 50)
	author = models.ForeignKey(members, null=True, blank=True)
	discussion = models.ForeignKey(post,null=True, blank = True)

class skills(models.Model):
	skill = models.CharField(max_length = 50)
	mem = models.ForeignKey(members,null = True, blank = True)

class interests(models.Model):
	interest = models.CharField(max_length = 50)
	mem = models.ForeignKey(members,null = True, blank = True)

class projects(models.Model):
	title = models.CharField(max_length = 50)
	description = models.TextField(max_length = 200)
	status = models.IntegerField(max_length = 1)
	mem = models.ForeignKey(members,blank = True, null = True)
