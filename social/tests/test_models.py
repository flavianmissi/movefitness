from django.test import TestCase

from social.models import Social


class SocialModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_a_social_networking_field(self):
        self.assertFieldPresence(Social, "social_networking")

    def test_should_have_a_profile_field(self):
        self.assertFieldPresence(Social, "profile")

    def test_unicode_should_return_social_network_and_profile_field(self):
        social = Social(social_networking="facebook", profile="someprofile")
        self.assertEqual("facebook/someprofile", unicode(social))
