from django.views.generic import ListView

from content.models import Content
from move_fitness.views import BaseView
from our_installations.models import OurInstallations


class OurInstallationsView(BaseView, ListView):

    template_name = "our_installations.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OurInstallationsView, self).get_context_data(*args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        our_installations = Content.objects.filter(slug="nossas-instalacoes") # should filter by slug
        context["installations_list"] = OurInstallations.objects.all()

        if our_installations.exists():
            context["content"] = our_installations[0]

        return context
