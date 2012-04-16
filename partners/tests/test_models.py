from django.test import TestCase

from partners.models import Partner


class PartnersModelTestCase(TestCase):

    def assertFieldPresence(self, model, field):
        self.assertIn(field, model._meta.get_all_field_names())

    def test_should_have_a_name_field(self):
        self.assertFieldPresence(Partner, "name")

    def test_should_have_a_url_field(self):
        self.assertFieldPresence(Partner, "url")

    def test_should_have_a_logo_field(self):
        self.assertFieldPresence(Partner, "logo")

    def test_unicode_should_return_the_partner_name(self):
        partner = Partner(name="me")
        self.assertEqual(u"me", unicode(partner))
