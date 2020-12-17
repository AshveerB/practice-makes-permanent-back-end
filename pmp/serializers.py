from rest_framework import serializers
from .models import Habits, Goals, Reflection


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = ('id', 'water', 'sleep', 'exercise', 'calories', 'learning', 'earning', 'spending', 'travel', 'date', 'owner_id')


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goals
        fields = ('id', 'water', 'sleep', 'exercise', 'calories', 'learning', 'earning', 'spending', 'travel', 'date', 'owner_id')


class ReflectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reflection
        fields = ('id', 'date', 'reflection', 'owner_id')
