from django.views.generic import ListView, DetailView

from activities.models import Activity
from content.models import Content
from move_fitness.views import BaseView


class ActivitiesView(ListView, BaseView):

    model = Activity
    context_object_name = "activities"
    template_name = "activities.html"

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        activities = Content.objects.filter(slug="atividades")
        if activities.exists():
            context["content"] = activities[0]
        return context


class ActivityView(DetailView, BaseView):

    model = Activity
    template_name = "activities.html"

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["activities"] = Activity.objects.all()
        context["content"] = context["object"]
        return context
