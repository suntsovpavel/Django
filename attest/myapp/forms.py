from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
 
class RecipeForm(forms.Form):        
    name = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=2000,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    cooking_steps = forms.CharField(max_length=2000,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    time_cooking = forms.TimeField(widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'type': 'time'
                               }))  
    image = forms.ImageField() 
    category = forms.MultipleChoiceField() 