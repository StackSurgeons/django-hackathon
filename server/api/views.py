from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hackathon
from .serializers import HackathonSerializer
from django.utils import timezone

class DashboardAPIView(APIView):
    def get(self, request):
        user = request.user
        active_hackathons = Hackathon.objects.filter(end_date__gte=timezone.now())
        past_hackathons = Hackathon.objects.filter(end_date__lt=timezone.now())

        active_hackathons_serializer = HackathonSerializer(active_hackathons, many=True)
        past_hackathons_serializer = HackathonSerializer(past_hackathons, many=True)

        data = {
            'active_hackathons': active_hackathons_serializer.data,
            'past_hackathons': past_hackathons_serializer.data,
        }

        return Response(data)

    def post(self, request):
        user = request.user
        hackathon_id = request.data.get('hackathon_id')

        try:
            hackathon = Hackathon.objects.get(id=hackathon_id)
        except Hackathon.DoesNotExist:
            return Response({'error': 'Hackathon does not exist.'}, status=404)

        # Check if the user is already participating in the hackathon
        if hackathon.participants.filter(id=user.id).exists():
            return Response({'error': 'User is already participating in the hackathon.'}, status=400)

        # Add the user to the hackathon participants
        hackathon.participants.add(user)
        hackathon.save()

        return Response({'success': 'User successfully joined the hackathon.'})
