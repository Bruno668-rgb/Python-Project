#Import of django libraries and import of classes already created in models and forms .py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db import IntegrityError
from .models import Funcionario
from .forms import FuncioanarioForm

#Creation of the POST, resquet and GET method for adding a new employee with their respective fields
def adicionar_funcionario(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        valor_hora = request.POST.get('valorHora')
        horas_trabalhadas = request.POST.get('horasTrabalhadas')
#Creation of a filtering object that checks whether an existing code matches the one being inserted
#No return it returns a warning from an existing employee with that code
        if Funcionario.objects.filter(codigo=codigo).exists():
            return render(request, 'adicionar_funcionario.html', {
                'error': 'Um funcionário com esse código já existe.'
            })

#Fill out all the fields, once completed it redirects you to the list of employees where all the information appears 
# in a table divided into columns#
        try:
            funcionario = Funcionario(
                codigo=codigo,
                nome=nome,
                valor_hora=valor_hora,
                horas_trabalhadas=horas_trabalhadas
            )
            funcionario.save()
            return redirect('listar_funcionario') 
        except IntegrityError:
            return render(request, 'adicionar_funcionario.html', {
                'error': 'Erro ao adicionar o funcionário. Tente novamente.'
            })
    return render(request, 'adicionar_funcionario.html')
#Creation of the method and objectlistar_funcionario, whose information comes from adicionar_funcionario
def listar_funcionario(request):
    #Here order the codes from smallest to largest
    funcionarios = Funcionario.objects.all().order_by('codigo')
#Here returns the information obtained in the adicionar_funcionario and puts it in the table that is divided into columns with the ones already provided
    return render(request, 'funcionarios/listar_funcionario.html', {'funcionarios': funcionarios})
#Creation of the request to delete an employee through his code (which contains all his information, entered in adicionar_funcionario)
def excluir_funcionario(request, codigo):
    #Here he sends a deletion request to the database
    try:
        funcionario = Funcionario.objects.get(codigo=codigo)
        #Delete function right after clicking the delete button on the listar_funcionario.html page
        funcionario.delete()
        #Here it returns the new table with the employee already deleted
        return redirect('listar_funcionario')
    #I created this part to find flaws in the delete method
    except Funcionario.DoesNotExist:
        return render(request, 'funcionario/listar_funcionario.html', {'error': 'Funcionario não encontrado'})
#Creation of the employee_edit function using a shortcut to access the primary key (pk)
def editar_funcionario(request, pk):
    #If it does not find the employee to perform the edit, it will give a 404 error
    funcionario = get_object_or_404(Funcionario, pk = pk)
    #Here there is a search for information that is filled in and a request to edit them made by instance
    #Just below, they are validated by form.is_valid(), which will be triggered when you click on the Save button, which is on the editar_funcionario.html page
    #If everything goes well, you will return to the listar_funcionario.html page with all the information changed
    #If an error occurs, it will just not save the information, this will occur when pressing the back button, where it keeps the information that is already there
    form = FuncioanarioForm(request.POST or None, instance=funcionario)
    if request.method == 'POST':
        form = FuncioanarioForm(request.POST, instance = funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionario')
        else:
            form = FuncioanarioForm(instance=funcionario)
    #Aqui ocorre o retorno das informações já editas para o formulario dos Funcionarios   
    return render(request, 'editar_funcionario.html', {'form': form, 'funcionario': funcionario})
#Here returns the access options to the pages mentioned above, through a main page which is index.html
def index(request):
    return render(request, 'index.html')
