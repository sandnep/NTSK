from django.db.models import fields
from django.forms import ModelForm
from .models import information

class inform(ModelForm):
    class Meta:
        model= information
        fields = ['lastname', 'firstname', 'middlename', 'contact', 'email', 'street', 'subd', 'brgy', 'city', 'zipcode', 'soapname', 'qty']
