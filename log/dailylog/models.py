from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    text = models.TextField()
    question_type = models.TextField()
    default = models.BooleanField()

    def __str__(self):
        return f'Question Text: {self.text} Question Type: {self.question_type}'

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    questions = models.ManyToManyField(Question, through='Answer')

    def __str__(self):
        return f'Created: {self.created}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Question: {self.question.text} Answer: {self.text}'
