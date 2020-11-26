from django.db import models
from PIL import Image
class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)
    address=models.TextField()
    state=models.CharField(max_length=30,blank=True)
    pin_code=models.IntegerField(blank=True)
    def __str__(self):
        return "Customer: "+self.username


