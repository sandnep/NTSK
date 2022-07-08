from django.db import models

class information(models.Model):
	lastname = models.CharField(max_length=300)	
	firstname = models.CharField(max_length=300)
	middlename = models.CharField(max_length=300)
	contact = models.IntegerField()
	email = models.EmailField(max_length=254, default="", blank=True, null=True)
	street= models.CharField(max_length=200)
	subd= models.CharField(max_length=200)
	brgy= models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	zipcode= models.IntegerField()
	soapname = models.CharField(max_length=300)	
	qty = models.CharField(max_length=300)


class Feedback(models.Model):
	message= models.TextField(max_length=200)


class ContactForm(models.Model):
	name = models.CharField(max_length=200)
	email= models.CharField(max_length=200)
	message= models.TextField(max_length=200)
