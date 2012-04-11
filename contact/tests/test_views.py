from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from contact.models import Contact
from contact.views import ContactView
from content.models import Content


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.content = Content.objects.create(title="foo", description="bar")
        self.contact = Contact.objects.create(
            address="some street",
            phone="222-2222",
            business_hours="8h as 19h"
        )
        self.request = RequestFactory().get("contact")
        self.response = ContactView.as_view()(self.request)

    def tearDown(self):
        if self.contact.id:
            self.contact.delete()
        self.content.delete()

    def test_should_request_and_be_success(self):
        self.assertEqual(200, self.response.status_code)

    def test_should_have_a_content_title_list_in_context(self):
        self.assertEqual("foo", self.response.context_data["content_list"][0]["title"])

    def test_should_have_one_contact_in_context(self):
        self.assertEqual("some street", self.response.context_data["contact"].address)

    def test_should_request_without_a_contact_and_be_success(self):
        self.contact.delete()
        response = ContactView.as_view()(self.request)
        self.assertEqual(200, response.status_code)

    def test_should_use_contact_template(self):
        self.assertIn("contact.html", self.response.template_name)


class ContactViewUrlTestCase(TestCase):

    def test_should_request_and_be_success(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(200, response.status_code)
