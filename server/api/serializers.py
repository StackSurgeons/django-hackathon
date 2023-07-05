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
    # participants = serializers.StringRelatedField(many=True)      
    is_active = serializers.ReadOnlyField()
    is_past = serializers.ReadOnlyField() 
    class Meta:
        model = Hackathon
        fields = '__all__'

# class HackathonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Hackathon
#         fields = ['name', 'start_date', 'end_date', 'visibility']
