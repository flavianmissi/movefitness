from django.test import TestCase, RequestFactory

from content.models import Content
from index.models import Image
from index.views import IndexView
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

    def test_should_have_all_content_titles_in_context(self):
        context_data = BaseView().get_context_data()
        self.assertEqual(context_data["content_list"][0]["title"], self.content.title)


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(title="foo", description="bar")
        self.image = Image.objects.create(description="something :P")
        self.request = RequestFactory().get("index")
        self.response = IndexView.as_view()(self.request)

    def tearDown(self):
        self.content.delete()
        self.image.delete()

    def test_should_get_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_use_index_template(self):
        self.assertIn("index.html", self.response.template_name)

    def test_should_have_a_content_list_in_context(self):
        self.assertEqual("foo", self.response.context_data["content_list"][0]["title"])

    def test_should_have_a_list_of_images(self):
        self.assertEqual(self.image.description, self.response.context_data["index_images"][0].description)
