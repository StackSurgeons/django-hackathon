from rest_framework import serializers
from .models import Leaderboard, Reward, ActiveUser, Hackathon


class MemberUsernameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username
    
class LeaderboardSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    membersname = MemberUsernameField(many=True, read_only=True)

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
    start_date = serializers.DateField(format='%Y-%m-%d')
    end_date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Hackathon
        fields = '__all__'

class HackathonJoinSerializer(serializers.Serializer):
    hackathon_id = serializers.IntegerField()
