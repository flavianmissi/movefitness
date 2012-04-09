from content.models import Content


class BaseView:

    model = Content

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['content_list'] = self.model.objects.all().values("title")
        return context
