# Generated by Django 2.2.5 on 2019-10-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_imageurl_downloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageurl',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]
