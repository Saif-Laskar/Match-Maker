# Generated by Django 3.2.4 on 2021-08-21 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20210821_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interestmodel',
            name='interest_education',
        ),
    ]
