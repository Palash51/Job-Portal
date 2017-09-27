from django.test import TestCase

# Create your tests here.

from .models import Document
from .forms import DocumentForm


class DocumentTest(TestCase):
	"""
	DocumentTest class will test model field and attributes. 
	"""

	def create_document(self, Name="palash", Email="palashpatidar51@gmail.com",Phone="7299851985",document="python.txt"):
		return Document.objects.create(Name=Name, Email=Email,Phone=7299851985)


	def test_document_creation(self):
		w = self.create_document()
		self.assertTrue(isinstance(w, Document))
		#self.assertEqual(w.__unicode__(), w.Name)


"""
test_valid_form will test fields and assert true if form is valid else test_invalid_form function will 
return false in case of invalidations. 
"""
def test_valid_form(self):
    w = Document.objects.create(Name="palash", Email="palashpatidar51@gmail.com",Phone="7299851985")
    data = {'Name': w.Name, 'Email': w.Email, 'Phone': w.Phone}
    form = DocumentForm(data=data)
    self.assertTrue(form.is_valid())

def test_invalid_form(self):
    w = Document.objects.create(title='Foo', body='')
    data = {'Name': w.Name, 'Email': w.Email, 'Phone': w.Phone}
    form = DocumentForm(data=data)
    self.assertFalse(form.is_valid())