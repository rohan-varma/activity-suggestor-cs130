from django.db import models


class ActivitySuggestion(models.Model):
	activaty_text = models.CharField(max_length = 200)
	date_suggested = models.DateTimeField('date suggested')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)