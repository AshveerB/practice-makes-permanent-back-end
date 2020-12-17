from django.shortcuts import render
from rest_framework import viewsets
from .models import Habits, Goals, Reflection
from .serializers import HabitSerializer, GoalSerializer, ReflectionSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Habits.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goals.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Goals.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReflectionViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionSerializer
    queryset = Reflection.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Reflection.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
