from django import forms
from .models import Pet
from django.contrib.auth.models import User



class PetOwnerForm(forms.ModelForm):
    class Meta:
        fields = ['type', 'name', 'birthday']