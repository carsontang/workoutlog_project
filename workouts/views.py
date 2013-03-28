from django.shortcuts import get_object_or_404
from django.shortcuts import render
from workouts.models import Exercise
from workouts.models import ExerciseSet
from workouts.models import Lift
from workouts.models import Workout

def index(request):
  latest_workouts = Workout.objects.all().order_by('-workout_date')[:5]
  context = { 'latest_workouts': latest_workouts }
  return render(request, 'workouts/index.html', context)

def show(request, workout_id):
  workout = get_object_or_404(Workout, pk=workout_id)
  m2a = {
    '03': 'Mar'
  }
  workout_month = workout.workout_date.strftime("%b")
  workout_date = workout.workout_date.strftime("%d")
  context = {
    'workout': workout,
    'workout_date': workout_date,
    'workout_month': workout_month
  }
  return render(request, 'workouts/show.html', context)