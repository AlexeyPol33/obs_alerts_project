from rest_framework.routers import DefaultRouter
from user_cabinet.views import UserViewSet


router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = router.urls