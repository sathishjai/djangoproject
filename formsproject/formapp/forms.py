from django import forms

class employeeinfoform(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()
    age=forms.IntegerField()
