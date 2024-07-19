from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from user_cabinet.models import User
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from rest_framework_simplejwt.tokens import RefreshToken
from user_cabinet.serializers import UserSerializer

def home(request):
    return HttpResponse('Home page')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    