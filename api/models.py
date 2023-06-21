from django.db import models

class Hackathon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    username = models.CharField(max_length=55)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.hackathon}"
    
class Winner(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    team = models.ForeignKey(Participant, on_delete=models.CASCADE)
    reward_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.hackathon.name} - {self.team.username}"
