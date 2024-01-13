from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import House
from .serializers import HouseSerializer
from django.http import Http404


class ListHouses(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    search_fields = ['title']


class ListUserHouses(generics.ListAPIView):
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return House.objects.filter(seller=self.request.user)


class DeleteUserHouse(generics.DestroyAPIView):
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return House.objects.filter(seller=self.request.user)


class UpdateUserHouse(generics.UpdateAPIView):
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return House.objects.filter(seller=self.request.user)


class CreateUserHouse(generics.CreateAPIView):
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ListCityHouses(generics.ListAPIView):
    serializer_class = HouseSerializer

    def get_queryset(self):
        city = self.kwargs['city']
        if not House.objects.filter(city=city).exists():
            raise Http404("City does not exist")
        return House.objects.filter(city=city)
