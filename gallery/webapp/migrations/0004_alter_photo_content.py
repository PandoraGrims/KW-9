# Generated by Django 4.2.4 on 2023-08-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_photo_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]