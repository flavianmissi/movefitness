from django.views.generic import DetailView

from content.models import Content


class BaseView(DetailView):

    model = Content

    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(*args, **kwargs)
        context['content_list'] = self.model.objects.all()
        return context
