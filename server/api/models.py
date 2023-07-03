from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()


    
class Reward(models.Model):
    hackthon_title = models.CharField(max_length=100)
    amt=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ActiveUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_active = models.DateTimeField()

class Hackathon(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    participants = models.ManyToManyField(User)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES,default="public")

    @property
    def is_active(self):
        current_datetime = timezone.now()
        return self.start_date <= current_datetime <= self.end_date
    
    @property
    def is_past(self):
        current_datetime = timezone.now()
        return current_datetime > self.end_date


