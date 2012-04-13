from django.views.generic import TemplateView

from index.models import Image
from move_fitness.views import BaseView


class IndexView(BaseView, TemplateView):

    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = TemplateView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["images_list"] = Image.objects.all()
        return context
