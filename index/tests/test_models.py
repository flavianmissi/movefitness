from django.test import TestCase

from index.models import Image


class ImageModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_a_description_field(self):
        self.assertFieldPresence(Image, "description")

    def test_should_have_a_photo_field(self):
        self.assertFieldPresence(Image, "photo")

    def test_unicode_should_return_description_field(self):
        image = Image(description="some description")
        self.assertEqual("some description", unicode(image))
