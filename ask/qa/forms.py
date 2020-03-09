from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        user, _ = User.objects.get_or_create(username='x',
                                             defaults={'password': 'y', 'last_login': timezone.now()})
        self.cleaned_data['author'] = user

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        user, _ = User.objects.get_or_create(username='x',
                                             defaults={'password': 'y', 'last_login': timezone.now()})
        self.cleaned_data['author'] = user

    def save(self):
        Answer.objects.create(**self.cleaned_data)


class RegUserForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('пользователь с таким именем уже зарегистрирован')
        return username

    def save(self):
        return User.objects.create(**self.cleaned_data, last_login=timezone.now())

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
