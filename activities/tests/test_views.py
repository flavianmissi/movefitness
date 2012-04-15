from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from activities.views import ActivitiesView, ActivityView
from activities.models import Activity
from content.models import Content


class ActivitieViewsTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('activities')
        self.content = Content.objects.create(
            title="Atividades",
            description="foo bar",
            slug="atividades"
        )
        self.activity = Activity.objects.create(
            title="do nothing",
            description="yes, that's a valid activity'"
        )
        self.response = ActivitiesView.as_view()(self.request)

    def tearDown(self):
        if self.content.id:
            self.content.delete()
        self.activity.delete()

    def test_should_get_acitivities_view_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_get_activities_and_have_the_content_record_referenced_to_it(self):
        self.assertIsInstance(self.response.context_data["content"], Content)

    def test_should_have_a_list_of_activities_in_the_context(self):
        self.assertIsInstance(self.response.context_data["activities"][0], Activity)

    def test_should_use_template_named_activities(self):
        self.assertIn("activities.html", self.response.template_name)

    def test_should_not_get_error_when_theres_no_content_activity_in_the_database(self):
        self.content.delete()
        response = ActivitiesView.as_view()(self.request)
        self.assertEqual(200, response.status_code)


class ActivitiesUrlTestCase(TestCase):

    def test_should_request_activities_page_and_be_success(self):
        response = self.client.get(reverse('activities'))
        self.assertEqual(200, response.status_code)


class ActivityViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('activity')
        self.content = Content.objects.create(
            title="Atividades",
            description="foo bar",
            slug="atividades"
        )
        self.activity = Activity.objects.create(
            title="do nothing",
            description="yes, that's a valid activity'",
            slug="do-nothing"
        )
        self.response = ActivityView.as_view()(self.request, slug=self.activity.slug)

    def tearDown(self):
        self.content.delete()
        self.activity.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_get_activity_and_call_it_content_in_context(self):
        self.assertIsInstance(self.response.context_data["content"], Activity)

    def test_should_have_activities_list_in_context(self):
        self.assertIsInstance(self.response.context_data["activities"][0], Activity)


    def test_should_use_activities_template(self):
        self.assertIn("activities.html", self.response.template_name)


class ActivityUrlTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(
            title="Atividades",
            description="foo bar",
            slug="atividades"
        )
        self.activity = Activity.objects.create(
            title="do nothing",
            description="yes, that's a valid activity'",
            slug="do-nothing"
        )

    def tearDown(self):
        self.content.delete()
        self.activity.delete()

    def test_should_request_and_be_success(self):
        response = self.client.get(reverse("activity", args=[self.activity.slug]))
        self.assertEqual(200, response.status_code)
