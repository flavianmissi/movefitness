from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from content.models import Content
from our_installations.models import OurInstallations
from our_installations.views import OurInstallationsView


class OurInstallationsViewsTestCase(TestCase):

    def setUp(self):
        self.installation = OurInstallations.objects.create(
            title="main entrance",
            slug="main-entrance"
        )
        self.content = Content.objects.create(title="foo", description="bar")
        self.our_installations = Content.objects.create(
            title="Our Installations",
            description="Lorem ipsum.",
            slug="nossas-instalacoes"
        )
        self.request = RequestFactory().get('our_installations')
        self.response = OurInstallationsView.as_view()(self.request)

    def tearDown(self):
        self.installation.delete()
        self.content.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_a_list_of_content_titles_in_context(self):
        self.assertEqual(self.response.context_data['content_list'][0]['title'], "foo")

    def test_should_have_the_our_installations_content_in_context(self):
        self.assertEqual(self.response.context_data['content'].title, "Our Installations")
        self.assertEqual(self.response.context_data['content'].description, "Lorem ipsum.")

    def test_should_have_installations_list_in_context(self):
        self.assertEqual(self.response.context_data['installations_list'][0].title, "main entrance")
        self.assertEqual(self.response.context_data['installations_list'][0].slug, "main-entrance")

    def test_should_use_our_installations_template(self):
        self.assertIn("our_installations.html", self.response.template_name)


class OurInstallationsUrlTestCase(TestCase):

    def test_should_request_and_be_success(self):
        response = self.client.get(reverse("our_installations"))
        self.assertEqual(200, response.status_code)
