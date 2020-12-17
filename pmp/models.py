from django.db import models
from users.models import User

# Create your models here.


class Habits(models.Model):
    water = models.PositiveSmallIntegerField()
    sleep = models.PositiveSmallIntegerField()
    exercise = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()
    learning = models.PositiveSmallIntegerField()
    spending = models.PositiveSmallIntegerField()
    earning = models.PositiveSmallIntegerField()
    travel = models.PositiveSmallIntegerField()
    date = models.DateField(unique=True)
    owner = models.ForeignKey(
        User, related_name='owned_habits', on_delete=models.CASCADE, default='owner habits')

    def __str__(self):
        return self.date


class Goals(models.Model):
    water = models.PositiveSmallIntegerField()
    sleep = models.PositiveSmallIntegerField()
    exercise = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()
    learning = models.PositiveSmallIntegerField()
    spending = models.PositiveSmallIntegerField()
    earning = models.PositiveSmallIntegerField()
    travel = models.PositiveSmallIntegerField()
    date = models.DateField(unique=True)
    owner = models.ForeignKey(
        User, related_name='owned_goals', on_delete=models.CASCADE, default='owner goals')

    def __str__(self):
        return self.water


class Reflection(models.Model):
    date = models.DateField(unique=True)
    reflection = models.TextField()
    owner = models.ForeignKey(
        User, related_name='owned_reflections', on_delete=models.CASCADE, default='owner reflections')

    def __str__(self):
        return self.date
