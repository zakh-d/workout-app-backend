from rest_framework import viewsets

from workouts.models import Workout
from workouts.serializers import WorkoutSerializer


class WorkoutsApiView(viewsets.ModelViewSet):

    serializer_class = WorkoutSerializer
    queryset = Workout.objects.all()
