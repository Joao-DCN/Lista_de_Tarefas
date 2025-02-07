from tkinter.tix import STATUS
from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):

    STATUS = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.
