from django import forms
from .models import ShivamBytes


# creating a form
class ShivamBytesForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = ShivamBytes

		# specify fields to be used
		fields = [
			"name",
			"city",
		]
