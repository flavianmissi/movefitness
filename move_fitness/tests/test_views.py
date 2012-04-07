from django.test import TestCase, RequestFactory

from content.models import Content
from move_fitness.views import BaseView


class BaseViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(
            title="foo",
            description="bar",
            slug="foo"
        )
        self.request = RequestFactory().get('base-view')
        self.response = BaseView.as_view()(self.request, slug=self.content.slug)

    def tearDown(self):
        self.content.delete()

    def test_should_get_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_all_contents_in_context(self):
        self.assertIsInstance(self.response.context_data["content_list"][0], Content)
