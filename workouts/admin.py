from django.contrib import admin
from workouts.models import Exercise, ExerciseSet, Lift, Workout

class ExerciseSetAdmin(admin.ModelAdmin):
  list_display = ('exercise', 'weight', 'number_of_sets', 'number_of_reps')
  list_filter = ['weight']

class ExerciseSetInline(admin.TabularInline):
  model = ExerciseSet
  extra = 0

class ExerciseAdmin(admin.ModelAdmin):
  inlines = [ExerciseSetInline]

class ExerciseInline(admin.TabularInline):
  model = Exercise
  extra = 0

class WorkoutAdmin(admin.ModelAdmin):
  inlines = [ExerciseInline]

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseSet, ExerciseSetAdmin)
admin.site.register(Lift)
admin.site.register(Workout, WorkoutAdmin)