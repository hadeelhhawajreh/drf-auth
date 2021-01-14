from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView
from .permissions import PermissionsClass
from .serializer import HealthSerializer
from .models import Health

from rest_framework.permissions import IsAuthenticated
# Create your views here.


class HealthListView(ListAPIView,CreateAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    # permission_classes=(PermissionsClass,)
    permission_classes=(PermissionsClass,IsAuthenticated)


class HealthDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    permission_classes=(PermissionsClass,IsAuthenticated)


# class 