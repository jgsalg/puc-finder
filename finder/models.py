from django.db import models

# Create your models here.

class Disciplina(models.Model):
    codigo_disc = models.CharField(max_length= 7, default = 'INF0000', primary_key=True)
    nome_disc = models.CharField(max_length= 50)
    qtt_provas = models.PositiveSmallIntegerField(default = 0)
    qtt_listas = models.PositiveSmallIntegerField(default = 0)
    def __str__(self):
        return self.nome_disc

class Exercicios(models.Model):
    id_ex = models.BigAutoField(primary_key=True, default = 0)
    nomearq = models.CharField(max_length=7)
    arq = models.BinaryField()
    data_submit = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default = False)
    codigo_disc = models.ForeignKey(Disciplina, default = 'INF0000', on_delete=models.CASCADE)
    def __str__(self):
        return self.nomearq

class Admin(models.Model):
    id_adm = models.BigAutoField(primary_key=True, default = 0)
    username = models.CharField(max_length = 50)
    senha = models.CharField(max_length = 50)
    def __str__(self):
        return self.username

class Aprova(models.Model):
    id_aprova = models.BigAutoField(primary_key=True, default = 0)
    id_adm = models.ForeignKey(Admin, on_delete=models.CASCADE)
    id_ex = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_aprova