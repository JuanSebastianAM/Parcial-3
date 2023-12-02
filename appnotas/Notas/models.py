from django.db import models


class Nota(models.Model):
    Titulo = models.CharField(max_length=30)
    Nota = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Titulo
    