# Generated by Django 2.0.10 on 2019-05-03 03:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_auto_20190502_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='footerContent',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
