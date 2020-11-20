from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, primary_key=True)
    date_of_birth = models.DateField('Birth Date')
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        ordering = ["first_name"]

