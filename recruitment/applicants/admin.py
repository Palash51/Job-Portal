from django.contrib import admin

# Register your models here.
from recruitment.applicants.models import Document

class DocumentAdmin(admin.ModelAdmin):
	"""
	DocumentAdmin class will represnt model interface for admin,
	only admin can acces it with admin credetials(super users).
	with admin actions.
	"""
	list_display = ('Name','Email','Phone','document','status')
	list_filter = ('Name','uploaded_at')
	search_fields = ('Name','Email')

admin.site.register(Document, DocumentAdmin)
