from django.test import TestCase

from our_installations.models import OurInstallations


class OurInstallationsModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_an_image_field(self):
        self.assertFieldPresence(OurInstallations, "photo")

    def test_should_have_a_description(self):
        self.assertFieldPresence(OurInstallations, "title")

    def test_unicode_should_return_the_title(self):
        installation = OurInstallations(title="foo")
        self.assertEqual(u'foo', unicode(installation))

    def test_should_pluralize_correctly_the_model_name(self):
        self.assertEqual(u'our installations', unicode(OurInstallations._meta.verbose_name_plural))
