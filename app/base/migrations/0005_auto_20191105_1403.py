# Generated by Django 2.2.6 on 2019-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_imagepersonannotation_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='path',
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
