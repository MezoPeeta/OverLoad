# Generated by Django 3.0.2 on 2020-01-30 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='authoer',
        ),
    ]
