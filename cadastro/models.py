from django.db import models

class Cadastro(models.Model):
    requerente = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    numero_do_processo = models.CharField(max_length=15)
    ano = models.IntegerField()
    data_do_processo = models.DateField()
    data_do_recebimento = models.DateField()
    responsavel = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

def __str__(self):
    return self.requente
