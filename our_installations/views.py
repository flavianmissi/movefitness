from django.views.generic import ListView

from move_fitness.views import BaseView
from content.models import Content


class OurInstallationsView(BaseView, ListView):

    template_name = "our_installations.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OurInstallationsView, self).get_context_data(*args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["content"] = Content.objects.filter(slug="nossas-instalacoes") # should filter by slug
        return context
