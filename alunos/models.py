from django.core.validators import MaxLengthValidator
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    bio = models.TextField(max_length=280, validators=[MaxLengthValidator(280)])

    def __str__(self):
        return self.nome
