from django.contrib import admin
from django.urls import path, include
from user_cabinet.views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_cabinet.urls')),
    path('api/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(),name='token_refresh'),
    path('', home)
]
