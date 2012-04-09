from django.test import TestCase

from content.models import Content
from move_fitness.views import BaseView


class BaseViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(
            title="foo",
            description="bar",
            slug="foo"
        )

    def tearDown(self):
        self.content.delete()

    def test_should_have_all_contents_in_context(self):
        context_data = BaseView().get_context_data()
        self.assertIsInstance(context_data["content_list"][0], Content)
