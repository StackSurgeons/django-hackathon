from django.contrib import admin
from . models import *

@admin.register(Hackathon)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'description','is_private','start_date','end_date']

@admin.register(Participant)
class hackadmin(admin.ModelAdmin):
    list_display=["id","username",'hackathon',"joined_at"]

@admin.register(Winner)
class hackadmin(admin.ModelAdmin):
    list_display=["id","hackathon",'team',"reward_amount"]