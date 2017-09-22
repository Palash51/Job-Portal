from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='description',
            new_name='Email',
        ),
        migrations.AddField(
            model_name='document',
            name='Name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='document',
            name='Phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
