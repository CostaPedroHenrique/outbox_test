from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    

    def __str__(self):
        return self.titulo