from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=30)
    user_pwd = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_birth = models.IntegerField()
    user_gender = models.CharField(max_length=5)
    user_email = models.CharField(max_length=40)
    user_phone = models.CharField(max_length=13)
    c_date = models.DateTimeField(null=True)