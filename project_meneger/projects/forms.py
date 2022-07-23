from dataclasses import field
from django.forms import ModelForm
from .models import *

class Edit_form(ModelForm):
    class Meta:
        model=Project
        fields='__all__'