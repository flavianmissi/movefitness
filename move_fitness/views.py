from content.models import Content
from social.models import Social


class BaseView:

    model = Content

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['content_list'] = self.model.objects.all().values("title")
        context["social"] = Social.all_as_dict()

        return context
