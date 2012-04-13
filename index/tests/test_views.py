from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from content.models import Content
from index.models import Image
from index.views import IndexView


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
        self.assertEqual(self.image.description, self.response.context_data["images_list"][0].description)


class IndexViewUrlsTestCase(TestCase):

    def test_should_get_and_be_success(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(200, response.status_code)
