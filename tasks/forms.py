from django import forms
from .models import Task

class FormularioCrearTarea(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write a title'}),
        'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'write a description'}),
        'important': forms.CheckboxInput(attrs={'class': 'form-check-input' 'm-auto mb-4'})
        }





    # title = forms.CharField(label = 'title')
    # description = forms.Textarea()
    # important = forms.CheckboxInput()

    # title.widget.attrs['class'] = 'form-control'
    # description.attrs['class'] = 'form-control'
    # important.attrs['class'] = 'form-check-input'
