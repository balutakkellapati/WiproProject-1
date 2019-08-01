from django.db import models
from users.models import CustomUser

class Category(models.Model):
	name = models.CharField(max_length=120)

class Question(models.Model):
	name = models.CharField(max_length=120)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	category_name = models.CharField(max_length=120, default= "default")


class Organization(models.Model):
	name = models.CharField(max_length=120)
	OrgLocation = models.CharField(max_length=120)
	OrgSize = models.CharField(max_length=120)
	OrgDomain = models.CharField(max_length=120)

class Assessment(models.Model):
	org_ID = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
	user_ID = models.CharField(max_length=120)
	time_stamp = models.DateTimeField(auto_now_add=True)

class questions_list(models.Model):
	assessment_ID = models.ForeignKey(Assessment, on_delete=models.SET_NULL, null=True)
	rating = models.CharField(max_length=120)
	question_ID = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
	question_name = models.CharField(max_length=120)
	question_category_name = models.CharField(max_length=120)