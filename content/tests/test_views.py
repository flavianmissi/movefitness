from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from content.models import Content
from content.views import ContentView


class ContentViewsTestCase(TestCase):

    def setUp(self):
        self.activities = Content.objects.create(
            title="Activities",
            description="Lorem ipsum dolor sit amet.",
            slug="activities"
        )
        self.request = RequestFactory().get("content")

    def tearDown(self):
        self.activities.delete()

    def test_should_request_the_view_for_a_content_and_be_success(self):
        response = ContentView.as_view()(self.request, slug=self.activities.slug)
        self.assertEqual(200, response.status_code)

    def test_should_render_the_template_based_on_the_objects_slug(self):
        response = ContentView.as_view()(self.request, slug=self.activities.slug)
        self.assertListEqual(["%s.html" % self.activities.slug], response.template_name)


class ContentViewUrlsTestCase(TestCase):

    def setUp(self):
        self.activities = Content.objects.create(
            title="Activities",
            description="Lorem ipsum dolor sit amet.",
            slug="activities"
        )
        self.client.get(reverse("content", args=[self.activities.slug]))

    def test_should_get_the_url_for_a_content_that_has_a_template_and_be_success(self):
        pass
