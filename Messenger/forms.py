from django import forms

class RegisterForm(forms.Form):
    Name= forms.CharField(label='Name', max_length=100)
    Username=forms.CharField(label='Username' , max_length=100)
    Contact=forms.CharField(label='Contact' , max_length=100)
    Password = forms.CharField(label='Password' , max_length=32, widget=forms.PasswordInput)