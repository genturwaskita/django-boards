from django.test import TestCase
from ..forms import SignUpForm

class SignUpFormTest(TestCase):
	def test_form_has_fields(self):
		form = SignUpForm()
		expacted = ['username', 'email', 'password1', 'password2']
		actual = list(form.fields)
		self.assertSequenceEqual(expacted, actual)