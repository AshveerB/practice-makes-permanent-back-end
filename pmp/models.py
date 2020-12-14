from django.db import models

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
    date = models.DateField(unique=True, auto_now_add=True)

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

    def __str__(self):
        return self.water


class Reflection(models.Model):
    date = models.DateField(unique=True, auto_now_add=True)
    reflection = models.TextField()

    def __str__(self):
        return self.date
