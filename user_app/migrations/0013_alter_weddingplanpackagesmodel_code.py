# Generated by Django 3.2.4 on 2021-08-21 16:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0012_alter_weddingplanpackagesmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingplanpackagesmodel',
            name='code',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=10, null=True, unique=True),
        ),
    ]
