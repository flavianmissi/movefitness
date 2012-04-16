from django.template import Context, Template
from django.test import TestCase


class MenuTemplateTagTestCase(TestCase):

    def test_should_make_a_menu_link_as_active(self):
        html = "{% load menu %}{% is_active request.get_full_path 'index' %}"
        template = Template(html)
        context = Context({'request': {"get_full_path": "/"}})

        self.assertEqual("active", template.render(context))

    def should_make_a_menu_link_as_not_active(self):
        html = "{% is_active request.get_full_path 'index' %}"
        template = Template(html)
        context = Context({'request': {"get_full_path": "register"}}) 
        self.assertNotEqual("active", template.render(context))
