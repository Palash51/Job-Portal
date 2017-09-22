from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0003_auto_20170921_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(blank=True, choices=[('yes', 'shortlisted'), ('no', 'rejected')], max_length=3),
        ),
    ]
