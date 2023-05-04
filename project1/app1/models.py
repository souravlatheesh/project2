from django.db import models

class userdata(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Place=models.CharField(max_length=50)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    OldPassword=models.CharField(max_length=50)
    NewPassword=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50)

