from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hackathon, Participant,Winner
from .serializers import HackathonSerializer, ParticipantSerializer,WinnerSerializer
from rest_framework.generics import ListAPIView,CreateAPIView


class HackathonList(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonCreate(CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class ParticipantList(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class ParticipantCreate(CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer


class WinnersList(ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class WinnersCreate(CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

