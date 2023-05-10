from django.forms import ModelForm
from .models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'birth']
        # fields = '__all__' #todos los campos
        labels = {'firstname': 'Ingrese el nombre'}
