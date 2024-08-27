from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from user_cabinet.models import User, DonationBar, MessageAlert
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from rest_framework_simplejwt.tokens import RefreshToken
from user_cabinet.serializers import UserSerializer, DonationBarSerializer, MessageAlertSerializer

def home(request):
    return HttpResponse('Home page')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DonationBarViewSet(ModelViewSet):
    queryset = DonationBar.objects.all()
    serializer_class = DonationBarSerializer

class MessageAlertViewSet(ModelViewSet):
    queryset = MessageAlert.objects.all()
    serializer_class = MessageAlertSerializer
