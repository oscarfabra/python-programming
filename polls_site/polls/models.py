import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
  # Class variables
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date published")
  # String representation
  def __str__(self):
    return self.question_text
  # Tells whether this question was published within the last day
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
  # Class variables
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  # String representation
  def __str__(self):
    return self.choice_text