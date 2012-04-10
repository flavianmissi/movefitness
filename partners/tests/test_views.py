from django.test import TestCase, RequestFactory

from content.models import Content
from partners.models import Partner
from partners.views import PartnerView


class PartnerViewTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('partners')
        self.response = PartnerView.as_view()(self.request)
        self.content = Content.objects.create(title="foo", description="bar")
        self.partner = Partner.objects.create(name="uau.impressos")

    def tearDown(self):
        self.content.delete()
        self.partner.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_content_titles_in_context(self):
        self.assertEqual("foo", self.response.context_data["content_list"][0]["title"])

    def test_should_have_partners_list_in_content(self):
        self.assertEqual("uau.impressos", self.response.context_data["partners"][0].name)
