#from django.views.generic import DetailView

from content.models import Content
from move_fitness.views import BaseView


class ContentView(BaseView):
    model = Content

    def get_template_names(self):
        return ["%s.html" % self.object.slug]
