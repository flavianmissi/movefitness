from django.test import TestCase

from content.models import Content


class OurInstallationModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_a_description_field(self):
        self.assertFieldPresence(Content, "description")

    def test_should_have_a_title_field(self):
        self.assertFieldPresence(Content, "title")

    def test_should_have_a_slug_field(self):
        self.assertFieldPresence(Content, "slug")

    def test_unicode_should_return_the_content_title(self):
        content = Content(title="Activities")
        self.assertEqual(unicode(content), u"Activities")
