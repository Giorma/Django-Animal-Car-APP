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


def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    animal.delete()
    return HttpResponse(f'Animal {animal.name} deleted successfully!')


class AnimalListView(ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animal_list.html'
