from django.db import models


class User(models.Model):
    full_name= models.CharField(max_length=50)
    email = models.EmailField(max_length=100, primary_key=True)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"

