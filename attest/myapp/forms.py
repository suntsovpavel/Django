from django import forms
from .models import Category

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    
class RecipeForm(forms.Form):        
    name = forms.CharField(max_length=100, required=True)
    desc = forms.CharField(max_length=2000, required=True,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    cooking_steps = forms.CharField(max_length=2000, required=True,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    time_cooking = forms.TimeField(required=True, widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'type': 'time'
                               }))  
    image = forms.ImageField() 
    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), 
                                         choices=set((x.name, x.name) for x in Category.objects.all()))  