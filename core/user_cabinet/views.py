from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from user_cabinet.models import User, DonationBar, MessageAlert
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from rest_framework_simplejwt.tokens import RefreshToken
from user_cabinet.serializers import UserSerializer, DonationBarSerializer, MessageAlertSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permissions import isAccountOwnerPermission

def home(request):
    return HttpResponse('Home page')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = list()
        match self.action:
            case 'list':
                permission_classes.append(IsAdminUser)
            case 'create':
                permission_classes.append(AllowAny)
            case 'retrieve':
                permission_classes.append(isAccountOwnerPermission)
            case 'update':
                permission_classes.append(isAccountOwnerPermission)
            case 'partial_update':
                permission_classes.append(isAccountOwnerPermission)
            case 'destroy':
                permission_classes.append(IsAdminUser)
        return [permission() for permission in permission_classes]

class DonationBarViewSet(ModelViewSet):
    queryset = DonationBar.objects.all()
    serializer_class = DonationBarSerializer

    def get_permissions(self):
        match self.action:
            case 'list':
                pass
            case 'reate':
                pass
            case 'retrieve':
                pass
            case 'update':
                pass
            case 'artial_update':
                pass
            case 'destroy':
                pass
            case _:
                return []
        
        

class MessageAlertViewSet(ModelViewSet):
    queryset = MessageAlert.objects.all()
    serializer_class = MessageAlertSerializer

    def get_permissions(self):
        match self.action:
            case 'list':
                pass
            case 'reate':
                pass
            case 'retrieve':
                pass
            case 'update':
                pass
            case 'artial_update':
                pass
            case 'destroy':
                pass
