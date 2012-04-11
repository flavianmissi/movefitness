from django.test import TestCase

from contact.models import Contact


class ContactModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_an_address_field(self):
        self.assertFieldPresence(Contact, "address")

    def test_should_have_a_phone_field(self):
        self.assertFieldPresence(Contact, "phone")

    def test_should_have_a_business_hours_field(self):
        self.assertFieldPresence(Contact, "business_hours")

    def test_unicode_should_return_address(self):
        contact = Contact(address="foo")
        self.assertEqual(u"foo", unicode(contact))
