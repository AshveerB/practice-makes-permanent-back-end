from rest_framework import serializers
from .models import Habits, Goals, Reflection


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = ('water', 'sleep', 'exercise', 'calories', 'learning', 'earning', 'spending', 'travel', 'date')


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goals
        fields = ('water', 'sleep', 'exercise', 'calories', 'learning', 'earning', 'spending', 'travel')


class ReflectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reflection
        fields = ('date', 'reflection')
