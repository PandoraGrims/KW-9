# Generated by Django 4.2.4 on 2023-08-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_photo_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]