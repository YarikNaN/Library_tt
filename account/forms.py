from django import forms
from django.contrib.auth.models import User

from account.models import Reader, BBviser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    name = forms.CharField(label='Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=255)
    address = forms.CharField(label='Address', max_length=500)

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'address')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        # Создаем объект User
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Создаем объект Reader, связываем его с User и сохраняем
            Reader.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                surname=self.cleaned_data['surname'],
                address=self.cleaned_data['address']
            )
        return user



class SvRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    tab_id = forms.CharField(label='Tab_id', max_length=100)


    class Meta:
        model = User
        fields = ('username', 'tab_id')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        # Создаем объект User
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Создаем объект Reader, связываем его с User и сохраняем
            BBviser.objects.create(
                user=user,
                tab_id=self.cleaned_data['tab_id']
            )
        return user