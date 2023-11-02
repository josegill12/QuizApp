from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=100)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=200)

class Option(models.Model):
    question = models.ForeignKey(Question, related_name= 'options', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)