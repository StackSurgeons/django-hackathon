from rest_framework import viewsets
from .models import Leaderboard, Reward, ActiveUser, Hackathon
from .serializers import (
    LeaderboardSerializer,
    RewardSerializer,
    ActiveUserSerializer,
    HackathonSerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView


class DashboardAPIView(APIView):
    def get(self, request):
        leaderboard_data = Leaderboard.objects.all()
        reward_data = Reward.objects.all()
        active_user_data = ActiveUser.objects.all()
        hackathon_data = Hackathon.objects.all()

        leaderboard_serializer = LeaderboardSerializer(leaderboard_data, many=True)
        reward_serializer = RewardSerializer(reward_data, many=True)
        active_user_serializer = ActiveUserSerializer(active_user_data, many=True)
        hackathon_serializer = HackathonSerializer(hackathon_data, many=True)

        data = {
            'leaderboard': leaderboard_serializer.data,
            'rewards': reward_serializer.data,
            'active_users': active_user_serializer.data,
            'hackathons': hackathon_serializer.data
        }

        return Response(data)
