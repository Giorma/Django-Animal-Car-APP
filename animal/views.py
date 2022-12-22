from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Animal


def create_animal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        age = request.POST.get('age')
        animal = Animal.objects.create(name=name, species=species, age=age)
        return HttpResponse(f'Animal {animal.name} created successfully!')
    return render(request, 'create_animal.html')


def delete_animal(request):
    if request.method == 'POST':
        try:
            animal_id = request.POST['animal_id']
            animal = Animal.objects.get(pk=animal_id)
        except ObjectDoesNotExist:
            return HttpResponse('Animal does not exist, please check animal list')
        animal.delete()
        return HttpResponse(f'Animal with ID {animal_id} deleted successfully!')
    return render(request, 'delete_animal.html')


class AnimalListView(ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animal_list.html'
