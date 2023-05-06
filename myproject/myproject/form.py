from django import forms 

class userForms(forms.Form):
    num1 = forms.CharField()
    num2 = forms.CharField()
    email = forms.EmailField()