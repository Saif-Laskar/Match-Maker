# Generated by Django 3.2.4 on 2021-08-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0008_alter_weddingplanpackagesmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingplanpackagesmodel',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
