from __future__ import unicode_literals

from django.db import models

CANDIDATE_STATUS = (

	('yes', 'shortlisted'),
	('no', 'rejected'),
	)


class Document(models.Model):
	"""
	Document class is a table in db with Schema which has atrributes name,email,
	phone document and status.
	"""

	Name = models.CharField(max_length=30, blank=False)
	Email = models.CharField(max_length=255, blank=False)
	Phone = models.CharField(max_length=30, blank=False)
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=3,choices=CANDIDATE_STATUS,blank=True)


	# def __str__(self):
	# 	return self.Name
