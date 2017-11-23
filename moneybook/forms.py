from django import forms
from .models import Moneybook

class CreateMoneybookForm(forms.ModelForm):
    
    class Meta:
        model = Moneybook
        fields = '__all__'
