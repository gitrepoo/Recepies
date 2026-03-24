from django.db import models
from django.contrib.auth.models import User

class Recepie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )
    receipe = models.CharField(max_length=100)
    receipe_description = models.TextField() 
    receipe_image = models.ImageField(upload_to='recepie')

    def __str__(self):
        return self.user
    

class APILog(models.Model):
    auth_type = models.CharField(max_length=20, null=True, blank=True)
    app_name = models.CharField(max_length=50, blank=True, null=True)
    method = models.CharField(max_length=10)
    endpoint = models.CharField(max_length=200)
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.endpoint}  - {self.method}"