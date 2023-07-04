from django.contrib import admin
from . models import *

@admin.register(Hackathon)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'start_date','end_date',"visibility"]

@admin.register(ActiveUser)
class activeadmin(admin.ModelAdmin):
    list_display=["id","user",'last_active']

@admin.register(Reward)
class rewardadmin(admin.ModelAdmin):
    list_display=["id","hackthon_title",'amt','user']

@admin.register(Leaderboard)
class leaderboardadmin(admin.ModelAdmin):
    list_display=["id","user",'score']

