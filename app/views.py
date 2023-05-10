from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Person, Tweet
from .forms import PersonForm

def index_view(request):

    return render(request, 'index.html')


def person_view(request, person_id):
    person = Person.objects.filter(id=person_id).first()

    return render(request, 'person.html', {'person': person})
# def home(request):
#   return HttpResponse("<h1>Hola mundo!</h1>")


def persons_view(request):
    persons = Person.objects.all()
    tweets = Tweet.objects.all()

    return render(request, 'persons.html', {'persons': persons})


def person_delete(request, person_id):
    person = Person.objects.filter(id=person_id).first()
    person.delete()
    return redirect('person-all')


def person_create(request):
    form = PersonForm()

    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('person-all')
    return render(request, 'create_update_form.html',{
        "form": form,
        "submit_value": "Crear Persona"})

def tweets_view(request):
    tweets = Tweet.objects.all()

    return render(request, 'tweets.html', context={'tweets': tweets})


