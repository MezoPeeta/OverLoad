# Generated by Django 3.0.2 on 2020-01-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200126_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]
