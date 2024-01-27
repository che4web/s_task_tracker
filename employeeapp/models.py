from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="ФИО")
    def get_absolute_url(self):
        return f"/employee/{self.id}/"
    def __str__(self):
        return self.name
