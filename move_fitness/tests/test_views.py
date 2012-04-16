from django.test import TestCase

from content.models import Content
from social.models import Social
from move_fitness.views import BaseView


class BaseViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(
            title="foo",
            description="bar",
            slug="foo"
        )
        self.twitter = Social.objects.create(profile="flaviamissi", social_networking="twitter")

    def tearDown(self):
        self.content.delete()

    def test_should_have_all_content_titles_in_context(self):
        context_data = BaseView().get_context_data()
        self.assertEqual(context_data["content_list"][0]["title"], self.content.title)

    def test_should_have_socials_in_context(self):
        context_data = BaseView().get_context_data()
        self.assertEqual(context_data["social"]["twitter"], "flaviamissi")
