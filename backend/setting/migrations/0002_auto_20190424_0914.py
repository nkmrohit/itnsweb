# Generated by Django 2.0.10 on 2019-04-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
