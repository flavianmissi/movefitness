from django.test import TestCase

from activities.models import Activity


class ActivitiesModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_a_title_field(self):
        self.assertFieldPresence(Activity, "title")

    def test_should_have_a_description_field(self):
        self.assertFieldPresence(Activity, "description")

    def test_should_have_a_slug_field(self):
        self.assertFieldPresence(Activity, "slug")

    def test_unicode_should_return_activity_title(self):
        activity = Activity(title="Some Activity", description="test", slug="some-activity")
        self.assertEqual(u"Some Activity", unicode(activity))

    def test_verbose_name_plural_should_return_activities(self):
        self.assertEqual(u"activities", unicode(Activity._meta.verbose_name_plural))
