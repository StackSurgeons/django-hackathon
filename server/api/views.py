from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hackathon,Reward,Leaderboard,ActiveUser
from .serializers import HackathonSerializer,ActiveUserSerializer,RewardSerializer,ActiveUser,LeaderboardSerializer,HackathonJoinSerializer
from django.utils import timezone
from rest_framework.decorators import api_view

@api_view(["GET"])
def company_dashboard(request):
    user = request.user
    active_hackathons = Hackathon.objects.filter(end_date__gte=timezone.now())
    past_hackathons = Hackathon.objects.filter(end_date__lt=timezone.now())
    leaderboard=Leaderboard.objects.all()
    reward=Reward.objects.all()
    activeUser=ActiveUser.objects.all()

    active_hackathons_serializer = HackathonSerializer(active_hackathons, many=True)
    past_hackathons_serializer = HackathonSerializer(past_hackathons, many=True)
    leaderboardserializer=LeaderboardSerializer(leaderboard,many=True)
    rewardserializer=RewardSerializer(reward,many=True)
    activeUserserializer=ActiveUserSerializer(activeUser,many=True)

    data = {
            'active_hackathons': active_hackathons_serializer.data,
            'past_hackathons': past_hackathons_serializer.data,
            "Leaderbooard":leaderboardserializer.data,
            'reward': rewardserializer.data,
            "active user":activeUserserializer.data
    }
    return Response(data)


@api_view(["GET"])
def hacker_dashboard(request):
    user = request.user
    active_hackathons = Hackathon.objects.filter(end_date__gte=timezone.now())
    past_hackathons = Hackathon.objects.filter(end_date__lt=timezone.now())
    leaderboard=Leaderboard.objects.all()
    reward=Reward.objects.all()
    activeUser=ActiveUser.objects.all()

    active_hackathons_serializer = HackathonSerializer(active_hackathons, many=True)
    past_hackathons_serializer = HackathonSerializer(past_hackathons, many=True)
    leaderboardserializer=LeaderboardSerializer(leaderboard,many=True)
    rewardserializer=RewardSerializer(reward,many=True)
    activeUserserializer=ActiveUserSerializer(activeUser,many=True)

    data = {
            'active_hackathons': active_hackathons_serializer.data,
            'past_hackathons': past_hackathons_serializer.data,
            "Leaderbooard":leaderboardserializer.data,
            'reward': rewardserializer.data,
            "active user":activeUserserializer.data
    }
    return Response(data)

class HackathonJoinAPIView(APIView):
    def post(self, request):
        serializer = HackathonJoinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        hackathon_id = serializer.validated_data['hackathon_id']
        user = request.user
        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            return Response({'error': 'Hackathon does not exist.'}, status=404)
        if hackathon.is_past:
            return Response({'error': 'Hackathon is already in the past.'}, status=400)
        if hackathon.visibility == 'private' and hackathon.creator != user:
            return Response({'error': 'This is a private hackathon and you are not the creator.'}, status=403)
        return Response({'success': 'User successfully joined the hackathon.'})
    
class HackathonCreateAPIView(APIView):
    def post(self, request):
        serializer = HackathonSerializer(data=request.data)
        if serializer.is_valid():
            hackathon = serializer.save()
            return Response({'success': 'Hackathon created successfully.'}, status=201)
        return Response(serializer.errors, status=400)