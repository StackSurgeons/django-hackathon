from django.db import models

class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()


class Participant(models.Model):
    username = models.CharField(max_length=55)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    
class Winner(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    team = models.ForeignKey(Participant, on_delete=models.CASCADE)
    reward_amount = models.DecimalField(max_digits=10, decimal_places=2)
