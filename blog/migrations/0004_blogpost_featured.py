# Generated by Django 4.1.7 on 2023-03-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_meta_description_blogpost_meta_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]
