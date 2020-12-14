from django.db import models

# Create your models here.


class Habits(models.Model):
    water = models.IntegerField()
    sleep = models.IntegerField()
    exercise = models.IntegerField()
    calories = models.IntegerField()
    learning = models.IntegerField()
    spending = models.IntegerField()
    earning = models.IntegerField()
    travel = models.IntegerField()
    date = models.DateField(unique=True)


class Goals(models.Model):
    water = models.IntegerField()
    sleep = models.IntegerField()
    exercise = models.IntegerField()
    calories = models.IntegerField()
    learning = models.IntegerField()
    spending = models.IntegerField()
    earning = models.IntegerField()
    travel = models.IntegerField()


class Reflection(models.Model):
    date = models.DateField(unique=True)
    reflection = models.TextField()
