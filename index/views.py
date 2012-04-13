from django.views.generic import TemplateView

from move_fitness.views import BaseView


class IndexView(BaseView, TemplateView):

    template_name = "index.html"
