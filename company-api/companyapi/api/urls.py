from django.urls import include, path
from api.views import CompanyViewSet
from rest_framework.routers import DefaultRouter # type: ignore

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
urlpatterns = [
   path('', include(router.urls)),
]
