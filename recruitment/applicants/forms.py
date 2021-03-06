from django import forms

from recruitment.applicants.models import Document

from django.contrib.auth.models import User

class DocumentForm(forms.ModelForm):
	"""
	DocumentForm will create form which will take users details
	and field are name.email.phone and resume
	"""
	class Meta:
		model = Document
		fields = ('Name','Email','Phone', 'document', )
