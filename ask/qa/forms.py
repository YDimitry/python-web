from django import forms

from qa.models import Question


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

# class AnswerForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea)
#     question = Question()


