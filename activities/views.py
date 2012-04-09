from django.views.generic import ListView

from activities.models import Activity
from move_fitness.views import BaseView


class AcitivitiesView(ListView, BaseView):

    model = Activity
