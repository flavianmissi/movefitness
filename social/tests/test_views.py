from django.test import TestCase, RequestFactory

from content.models import Content
from social.views import SocialView


class SocialViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get("social")
        self.response = SocialView.as_view()(request)
        self.content = Content.objects.create(title="foo")

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_a_content_titles_list_in_the_context(self):
        self.assertEqual("foo", self.response.context_data["content_list"][0]["title"])
