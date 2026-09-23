from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AlunoForm
from .models import Aluno


def lista_alunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'alunos/lista.html', {'alunos': alunos})


def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cartão criado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/form.html', {'form': form, 'titulo': 'Novo Cartão'})


def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cartão atualizado com sucesso!')
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {'form': form, 'titulo': 'Editar Cartão'})


def excluir_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Cartão excluído com sucesso!')
        return redirect('lista_alunos')
    return render(request, 'alunos/confirmar_exclusao.html', {'aluno': aluno})
