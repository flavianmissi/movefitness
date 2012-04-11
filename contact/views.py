from django.views.generic import TemplateView

from contact.models import Contact
from move_fitness.views import BaseView


class ContactView(BaseView, TemplateView):

    template_name = "contact.html"

    def get_context_data(self, *args, **kwargs):
        context = TemplateView.get_context_data(self, *args, **kwargs)
        context.update(BaseView.get_context_data(self, *args, **kwargs))

        contacts = Contact.objects.all()
        if contacts.exists():
            context["contact"] = contacts[0]

        return context
