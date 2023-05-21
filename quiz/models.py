from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE : ForeignKey(Question)가 삭제되면 이 data(Ansewer)도 사라진다
    content = models.TextField()
    create_date = models.DateTimeField()
