from django import forms
from django.contrib.auth.models import User
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['pub_date','author']
        
        
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = []