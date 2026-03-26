from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)  # admin / user

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.username