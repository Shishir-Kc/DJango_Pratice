from django import forms


class StudentFrom(forms.Form):
    user_name = forms.CharField(max_length=100)
