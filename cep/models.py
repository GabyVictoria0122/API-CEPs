from django.db import models

# Create your models here.

class Cep(models.Model):
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=250, null=True)
    estado = models.CharField(max_length=250, null=True)
    bairro = models.CharField(max_length=250)
    rua = models.CharField(max_length=250)
    complemento = models.CharField(max_length=250, null=True)