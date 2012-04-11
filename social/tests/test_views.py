from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from content.models import Content
from social.views import SocialView


class SocialViewTestCase(TestCase):

    def setUp(self):
        self.news = Content.objects.create(
            title="news",
            description="some news",
            slug="noticias"
        )
        self.content = Content.objects.create(title="foo")
        self.request = RequestFactory().get("social")
        self.response = SocialView.as_view()(self.request)

    def tearDown(self):
        if self.news.id:
            self.news.delete()
        self.content.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_a_content_titles_list_in_the_context(self):
        self.assertEqual("foo", self.response.context_data["content_list"][1]["title"])

    def test_should_have_the_news_content_in_the_context(self):
        self.assertEqual("news", self.response.context_data["content"].title)
        self.assertEqual("noticias", self.response.context_data["content"].slug)
        self.assertEqual("some news", self.response.context_data["content"].description)

    def test_should_request_without_a_news_content_and_be_success(self):
        self.news.delete()
        response = SocialView.as_view()(self.request)
        self.assertEqual(200, response.status_code)

    def test_should_use_social_template(self):
        self.assertIn("social.html", self.response.template_name)


class SocialViewUrlTestCase(TestCase):

    def test_should_request_and_be_success(self):
        response = self.client.get(reverse("social"))
        self.assertEqual(200, response.status_code)
