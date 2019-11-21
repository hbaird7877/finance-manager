from django.urls import path, include
from .views import LoanViewSet, BorrowerViewSet, AddressViewSet, PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LoanViewSet, basename='loan')
router.register(r'', AddressViewSet, basename='address')
router.register(r'', BorrowerViewSet, basename='borrower')
router.register(r'', PaymentViewSet, basename='payment')
urlpatterns = router.urls