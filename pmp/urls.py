from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, GoalViewSet, ReflectionViewSet


router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'reflections', ReflectionViewSet, basename='reflection')
