from django.db import models

# Create your models here.

class customer(models.Model):
	rname = models.CharField(max_length=30)
	rlastname = models.CharField(max_length=30)
	remail = models.CharField(max_length=30)
	rphone = models.CharField(max_length=30)
	rperson = models.CharField(max_length=30)
	rtable = models.CharField(max_length=30)
	rdate = models.CharField(max_length=30)
	rtime = models.CharField(max_length=30)
	rcomment = models.CharField(max_length=50)

