from django.db.models import fields
from .models import *
from django import forms

class cusform(forms.ModelForm):
    class Meta:
        model = Customer
        fields='__all__'