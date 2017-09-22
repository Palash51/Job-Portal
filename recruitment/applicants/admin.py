from django.contrib import admin

# Register your models here.
from recruitment.applicants.models import Document

class DocumentAdmin(admin.ModelAdmin):
	list_display = ('Name','Email','Phone','document','status')
	list_filter = ('Name','uploaded_at')
	search_fields = ('Name','Email')

admin.site.register(Document, DocumentAdmin)
