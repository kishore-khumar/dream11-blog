# Generated by Django 3.1.1 on 2020-09-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200911_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='display',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
