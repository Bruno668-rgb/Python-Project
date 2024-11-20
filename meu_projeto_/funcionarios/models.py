from django.db import models
#Creation of the employee class that will use the information in the views.py files
#In this code it controls and limits information such as decimal places, the number of characters that the name can have, etc.
class Funcionario(models.Model):
    codigo = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)
    horas_trabalhadas = models.DecimalField(max_digits=10, decimal_places=2)
    #Here it sends the information when activated with a from .models import Funcionario
    def __str__(self):
        return self.nome