from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=2000,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    price = forms.DecimalField(max_digits=8, decimal_places=2)    
    amount = forms.IntegerField()
    date = forms.DateField(widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'type': 'date'
                               })) 
    image = forms.ImageField()

class ProductFormWithPK(forms.Form):
    pk = forms.IntegerField(min_value=1)        # задаем primary key изменяемого объекта 
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=2000,
                                widget=forms.Textarea(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter description'
                                }))
    price = forms.DecimalField(max_digits=8, decimal_places=2)    
    amount = forms.IntegerField()
    date = forms.DateField(widget=forms.DateInput(attrs={
                                   'class': 'form-control',
                                   'type': 'date'
                               })) 
    image = forms.ImageField()