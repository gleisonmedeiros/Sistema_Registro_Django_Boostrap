from django.db import models
from multiupload.fields import MultiMediaField


class Cadastro(models.Model):
    requerente = models.CharField(max_length=100)
    assunto = models.CharField(max_length=100)
    numero_do_processo = models.CharField(max_length=15,null=True,blank=True)
    ano = models.IntegerField(null=True,blank=True)
    data_do_processo = models.DateField(null=True,blank=True)
    data_do_recebimento = models.DateField(null=True,blank=True)
    responsavel = models.CharField(max_length=20,null=True,blank=True)
    status = models.CharField(max_length=30,null=True,blank=True)
    destino = models.CharField(max_length=100,null=True,blank=True)

class Imagem(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE,null=True,blank=True)
    imagem = models.ImageField(upload_to='images/', null=True, blank=True)
    pdf = models.FileField(upload_to='pdf/', null=True, blank=True)




def __str__(self):
    return self.requente
