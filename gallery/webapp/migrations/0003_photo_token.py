# Generated by Django 4.2.4 on 2023-08-26 10:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_albumphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
