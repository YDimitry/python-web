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

    def clean(self):
        user, _ = User.objects.get_or_create(username='x',
                                             defaults={'password': 'y', 'last_login': timezone.now()})
        self.cleaned_data['author'] = user

    def save(self):
        Answer.objects.create(**self.cleaned_data)
