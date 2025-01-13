from django import forms


class StudentFrom(forms.Form):
    user_name = forms.CharField(max_length=100 , label="Student Name = > ")
    user_pass = forms.CharField(widget=forms.PasswordInput())