from django.test import TestCase

from our_installations.models import OurInstallation


class OurInstallationModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_an_image_field(self):
        self.assertFieldPresence(OurInstallation, "photo")

    def test_should_have_a_description(self):
        self.assertFieldPresence(OurInstallation, "title")

    def test_unicode_should_return_the_title(self):
        installation = OurInstallation(title="foo")
        self.assertEqual(u'foo', unicode(installation))
