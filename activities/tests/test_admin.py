from django.test import TestCase
from django.contrib import admin

from activities.models import Activity
from activities.admin import ActivityAdmin


class ActivityAdminTestCase(TestCase):

    def test_should_register_Activity_model(self):
        self.assertIn(Activity, admin.site._registry)

    def test_should_register_Activity_model_with_OurInstallationAdmin_class(self):
        self.assertIsInstance(admin.site._registry[Activity], ActivityAdmin)

