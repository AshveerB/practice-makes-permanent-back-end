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

    def __str__(self):
        return self.date


class Goals(models.Model):
    water = models.IntegerField()
    sleep = models.IntegerField()
    exercise = models.IntegerField()
    calories = models.IntegerField()
    learning = models.IntegerField()
    spending = models.IntegerField()
    earning = models.IntegerField()
    travel = models.IntegerField()

    def __str__(self):
        return self.water


class Reflection(models.Model):
    date = models.DateField(unique=True)
    reflection = models.TextField()

    def __str__(self):
        return self.date
