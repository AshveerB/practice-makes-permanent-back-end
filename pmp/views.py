from django.shortcuts import render
from rest_framework import viewsets
from .models import Habits, Goals, Reflection
from .serializers import HabitSerializer, GoalSerializer, ReflectionSerializer

# Create your views here.


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goals.objects.all()


class ReflectionViewSet(viewsets.ModelViewSet):
    serializer_class = ReflectionSerializer
    queryset = Reflection.objects.all()
