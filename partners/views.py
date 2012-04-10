from django.views.generic import ListView

from move_fitness.views import BaseView
from partners.models import Partner


class PartnerView(BaseView, ListView):

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))
        context["partners"] = Partner.objects.all()
        return context
