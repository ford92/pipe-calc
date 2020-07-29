from django import forms

from .models import Pipe, Liner

class NameForm(forms.ModelForm):
	class Meta:
		model = Pipe
		fields = [
			'ex_diameter',
			'ex_construction',
			'ex_length',
			'ex_inlet',
			'ex_outlet',
			'pro_diameter',
			'pro_construction',
			'pro_length',
			'pro_inlet',
			'pro_outlet',
		]

class LinerForm(forms.ModelForm):
	class Meta:
		model = Liner
		fields = [
			'diameter',
			'shape',
			'distance',
		]

