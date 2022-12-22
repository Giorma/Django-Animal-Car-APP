from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from django.views.generic import ListView


def create_car(request):
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        car = Car.objects.create(make=make, model=model, year=year)
        return HttpResponse(f'Car {car.make} {car.model} created successfully!')
    return render(request, 'create_car.html')


def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car.delete()
    return HttpResponse(f'Car {car.make} {car.model} deleted successfully!')


class CarListView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'car_list.html'
