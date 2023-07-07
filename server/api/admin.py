from django.contrib import admin
from . models import *

@admin.register(Hackathon)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'start_date','end_date',"visibility","description","Reward","problem_statements","external_links"]
    
@admin.register(ActiveUser)
class activeadmin(admin.ModelAdmin):
    list_display=["id","user",'last_active']

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ["id", "display_hackathon_title", "amt", "display_participants"]

    def display_hackathon_title(self, obj):
        return obj.hackathon_title.name

    display_hackathon_title.short_description = "Hackathon Title"

    def display_participants(self, obj):
        return ", ".join([str(user) for user in obj.user.all()])

    display_participants.short_description = "Participants"


@admin.register(Leaderboard)
class leaderboardadmin(admin.ModelAdmin):
    list_display=["id","user",'score',"team"]

