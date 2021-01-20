import hashlib
import binascii
from django.db import models


class User(models.Model):
    full_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=100, primary_key=True)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100, null=False, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "users"
 
    def save(self, *args, **kwargs): 
        self.password = binascii.hexlify(self.password.encode()).decode()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


