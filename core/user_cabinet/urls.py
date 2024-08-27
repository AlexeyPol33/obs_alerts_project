from rest_framework.routers import DefaultRouter
from user_cabinet.views import UserViewSet, DonationBarViewSet, MessageAlertViewSet


router = DefaultRouter()
router.register('', UserViewSet)
router.register('DonationBar', DonationBarViewSet)
router.register('MessageAlert', MessageAlertViewSet)
urlpatterns = router.urls