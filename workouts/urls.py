from django.conf.urls import patterns, url

from workouts import views

urlpatterns = patterns('',
  # ex: /workouts
  url(r'^$', views.index, name='index'),

  # ex: /workouts/1/
  url(r'^(?P<workout_id>\d+)/$', views.show, name='show'),
)