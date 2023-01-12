from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


from .models import Position,Employees,User
from .serializers import PositionSerializer, UserSerializer, EmployeeSerializer


# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PositionApiViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = [DjangoFilterBackend,SearchFilter ]
    filterset_fields = ['post', 'department']
    search_fields = ['post', 'department']


class EmployeeApiViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    filter_backends = [SearchFilter,OrderingFilter]
    ordering_fields = ['name','salary']
    search_fields = ['name', ]
