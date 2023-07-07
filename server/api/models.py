from django.db import models,migrations
from django.contrib.auth.models import User
from django.utils import timezone

# class Leaderboard(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     score = models.IntegerField()
#     membersname = models.ManyToManyField(User.name, related_name='member_leaderboards')
#     highlighted = models.BooleanField(default=True)
#     team=models.CharField(max_length=20,null=False)

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    membersname = models.ManyToManyField(User, related_name='member_leaderboards')
    highlighted = models.BooleanField(default=True)
    team = models.CharField(max_length=20, null=False)



class ActiveUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_active = models.DateTimeField()

class Hackathon(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    # participants = models.ManyToManyField(User)
    description=models.CharField(max_length=200)
    Reward=models.IntegerField(default=1000)
    problem_statements=models.TextField()
    external_links=models.URLField(max_length=50,default="none")

    @property
    def is_active(self):
        current_date = timezone.now().date()
        return self.start_date <= current_date <= self.end_date

    @property
    def is_past(self):
        current_date = timezone.now().date()
        return current_date > self.end_date
    
class Reward(models.Model):
    hackathon_title = models.OneToOneField(Hackathon, on_delete=models.CASCADE)
    amt = models.IntegerField(default=0)
    user = models.ManyToManyField(User)

    
    class Meta:
        verbose_name_plural = "Rewards"



