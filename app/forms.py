from django import forms

class Studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField
    
