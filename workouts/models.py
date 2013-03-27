from django.conf import settings
from django.db import models

# Create your models here.
class Workout(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  workout_date = models.DateTimeField('workout date')

  def __unicode__(self):
    return self.workout_date.strftime("%A (%m/%d/%Y)")

class Lift(models.Model):
  lift_name = models.CharField(max_length=50)

  def __unicode__(self):
    return self.lift_name

class Exercise(models.Model):
  lift = models.ForeignKey(Lift)
  workout = models.ForeignKey(Workout)

  def __unicode__(self):
    workout_date = self.workout.workout_date.strftime('%A (%m/%d/%Y)')
    return "%(workout_date)s - %(lift_name)s" % { 'workout_date': workout_date, 'lift_name': self.lift.lift_name }

class ExerciseSet(models.Model):
  exercise = models.ForeignKey(Exercise)
  number_of_reps = models.IntegerField(default=1)
  number_of_sets = models.IntegerField(default=1)
  weight = models.IntegerField(default=0)

  def __unicode__(self):
    return "%(lift_name)s - %(weight)dlbs X %(number_of_sets)d X %(number_of_reps)d" % { 'lift_name': self.exercise.lift.lift_name, 'weight': self.weight, 'number_of_sets': self.number_of_sets, 'number_of_reps': self.number_of_reps}