# Generated by Django 2.2.15 on 2020-12-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_bboxannotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(max_length=270, unique=True, upload_to=''),
        ),
    ]