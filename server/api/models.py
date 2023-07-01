from django.db import models
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    participants = models.ManyToManyField(User)
    is_private=models.BooleanField(default=False)


