from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import Disciplina
from django.shortcuts import render, redirect
from django.db.models import Q


def index(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    disciplinas =  Disciplina.objects.filter(
        Q(nome_disc__icontains=q) | Q(codigo_disc__icontains=q))

    return render(request, 'home/index.html', {'disciplinas': disciplinas})


# def add_discipline(request):
#     new_discipline = Disciplina(
#         discipline_code='CS102',
#         discipline_name='Computer Science 102',
#         quantity_of_exams=3,
#         quantity_of_tests=4
#     )
#     new_discipline.save()
#     return HttpResponse('Discipline added successfully')

