from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE : ForeignKey(Question)가 삭제되면 이 data(Ansewer)도 사라진다
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
