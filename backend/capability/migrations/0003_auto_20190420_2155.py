# Generated by Django 2.0.10 on 2019-04-20 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capability', '0002_auto_20190420_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='capability',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
