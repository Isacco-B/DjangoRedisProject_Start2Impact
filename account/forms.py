from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ("username","email", "password", "password_confirm")

    def clean(self):
        super().clean()
        password = self.cleaned_data["password"]
        password_confrim = self.cleaned_data["password_confirm"]
        if password != password_confrim:
            raise  forms.ValidationError("passwords do not match")
        return self.cleaned_data




