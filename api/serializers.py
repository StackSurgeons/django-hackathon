from rest_framework import serializers
from .models import Hackathon, Participant, Winner

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'
