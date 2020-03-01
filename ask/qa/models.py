from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)  # заголовок вопроса
    text = models.TextField()  # полный текст вопроса
    added_at = models.DateField(blank=True, auto_now_add=True)  # дата добавления вопроса
    rating = models.IntegerField(default=0)  # рейтинг вопроса(число)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)  # автор вопроса
    likes = models.ManyToManyField(User, related_name='question_like_user')  # список пользователей, поставивших "лайк"


class Answer(models.Model):
    text = models.TextField()  # текст ответа
    added_at = models.DateField(blank=True, auto_now_add=True)  # дата добавления ответа
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)  # вопрос, к которому относится ответ
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)  # автор ответа
