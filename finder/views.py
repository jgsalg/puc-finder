from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .models import Disciplina

def index(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())


def add_discipline(request):
    new_discipline = Disciplina(
        discipline_code='CS102',
        discipline_name='Computer Science 102',
        quantity_of_exams=3,
        quantity_of_tests=4
    )
    new_discipline.save()
    return HttpResponse('Discipline added successfully')