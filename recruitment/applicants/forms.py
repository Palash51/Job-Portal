from django import forms

from recruitment.applicants.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('Name','Email','Phone', 'document', )
