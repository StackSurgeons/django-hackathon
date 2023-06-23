from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hackathon, Participant,Winner
from .serializers import HackathonSerializer, ParticipantSerializer,WinnerSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from rest_framework.views   import APIView

class HackathonList(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonCreate(CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class ParticipantList(ListAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class ParticipantCreate(CreateAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class WinnersList(ListAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer

class WinnersCreate(CreateAPIView):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
