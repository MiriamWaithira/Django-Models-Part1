from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# If any change is made in this file, the migrations must be made using: 'python manage.py migrations'.

# Create the classes
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    publish_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
