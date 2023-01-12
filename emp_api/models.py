from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Position(models.Model):
    post = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self):
        return f'Position : {self.post}, Department : {self.department}'

class Employees(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
