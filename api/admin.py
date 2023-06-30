from django.contrib import admin
from . models import *

@admin.register(Hackathon)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'start_date','end_date']

@admin.register(Leaderboard)
class hackadmin(admin.ModelAdmin):
    list_display=["id","user",'score']

@admin.register(ActiveUser)
class hackadmin(admin.ModelAdmin):
    list_display=["id","user",'last_active']

@admin.register(Reward)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'description','user']
