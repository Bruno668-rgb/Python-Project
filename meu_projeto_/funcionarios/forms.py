from .models import Funcionario
from django import forms
#The same thing happens here as in models.py, only the difference is that a Class was created where the information will be edited
#The jpa fields created were also called, but for a new Class called FunctionarioForm

class FuncioanarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['codigo', 'nome', 'valor_hora', 'horas_trabalhadas']