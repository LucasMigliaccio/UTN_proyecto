# Generated by Django 3.2.19 on 2023-09-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(max_length=255, upload_to='blog/images/'),
        ),
    ]
