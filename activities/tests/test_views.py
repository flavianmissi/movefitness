from django.test import TestCase, RequestFactory

from activities.views import AcitivitiesView


class ActivitiesViewsTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('activities')

    def test_should_get_acitivities_view_and_be_success(self):
        response = AcitivitiesView.as_view()(self.request)
        self.assertEqual(200, response.status_code)
