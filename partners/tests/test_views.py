from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from content.models import Content
from partners.models import Partner
from partners.views import PartnersView


class PartnersViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(title="partner", description="bar", slug="parceiros")
        self.partner = Partner.objects.create(name="uau.impressos")
        self.request = RequestFactory().get('partners')
        self.response = PartnersView.as_view()(self.request)

    def tearDown(self):
        self.content.delete()
        self.partner.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_content_titles_in_context(self):
        self.assertEqual("partner", self.response.context_data["content_list"][0]["title"])

    def test_should_have_partners_list_in_content(self):
        self.assertEqual("uau.impressos", self.response.context_data["partners"][0].name)

    def test_should_have_partner_content_in_context(self):
        self.assertEqual("partner", self.response.context_data["content"].title)
        self.assertEqual("parceiros", self.response.context_data["content"].slug)

    def test_should_use_partners_template(self):
        self.assertIn("partners.html", self.response.template_name)


class PartnersViewUrlTestCase(TestCase):

    def test_should_request_and_be_success(self):
        response = self.client.get(reverse("partners"))
        self.assertEqual(200, response.status_code)
