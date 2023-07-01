from rest_framework import serializers
from .models import Leaderboard, Reward, ActiveUser, Hackathon

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class ActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveUser
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'
