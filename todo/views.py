#from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import Task
from .serializers import (
    ListTaskSerializer,
    CreateTaskSerializer,
    RetrieveTaskSerializer,
    UpdateTaskSerializer,
    DestroyTaskSerializer,

)
# Create your views here.

class ListTaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ListTaskSerializer

class CreateTaskAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer

class RetrieveTaskApiView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = RetrieveTaskSerializer

class UpdateTaskAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class =  UpdateTaskSerializer

class DestroyTaskAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = DestroyTaskSerializer
