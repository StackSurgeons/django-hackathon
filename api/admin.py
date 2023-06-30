from django.contrib import admin
from . models import *

@admin.register(Hackathon)
class hackadmin(admin.ModelAdmin):
    list_display=["id","name",'description','is_private','start_date','end_date']
