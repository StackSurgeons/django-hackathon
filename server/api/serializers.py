from rest_framework import serializers
from .models import Leaderboard, Reward, ActiveUser, Hackathon

class LeaderboardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Leaderboard
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    hackathon_title = serializers.StringRelatedField(source='hackathon_title.name')

    class Meta:
        model = Reward
        fields = '__all__'

class ActiveUserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = ActiveUser
        fields = '__all__'

class HackathonSerializer(serializers.ModelSerializer):   
    is_active = serializers.ReadOnlyField()
    is_past = serializers.ReadOnlyField() 
    class Meta:
        model = Hackathon
        fields = '__all__'

class HackathonJoinSerializer(serializers.Serializer):
    hackathon_id = serializers.IntegerField()
