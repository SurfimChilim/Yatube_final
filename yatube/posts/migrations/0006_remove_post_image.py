# Generated by Django 2.2.16 on 2022-04-26 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
