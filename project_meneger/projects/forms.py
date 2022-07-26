from django import forms
from .models import *
import datetime

class Edit_form(forms.ModelForm):
    deadline=forms.DateField()
    class Meta:
        model=Project
        fields='__all__'
    def clean_deadline(self,*args,**kwargs):
        today=datetime.date.today()
        deadline=self.cleaned_data.get('deadline')
        if deadline <= today:
            raise forms.ValidationError('Deadline must be in the future.')
        return deadline