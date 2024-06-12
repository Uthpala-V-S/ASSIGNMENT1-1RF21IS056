from django import forms
class inputform1(forms.Form):
    n=forms.IntegerField(max_value=10,min_value=1,label="enter a number")