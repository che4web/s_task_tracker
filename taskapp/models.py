from django.db import models
from employeeapp.models import Employee

# Create your models here.

class Note(models.Model):
    text = models.TextField(verbose_name="Текст замект")

class Task(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Название задачи")
    done = models.BooleanField(verbose_name="Выполнена")
    deadlite = models.DateField(verbose_name="Срок выполнения")
    note = models.ForeignKey(Note,
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True)

    employee = models.ForeignKey(Employee,
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True)

    def get_absolute_url(self):
        return f"task/{self.id}/"
    def __str__(self):
        return f"{self.id}. {self.name}"


