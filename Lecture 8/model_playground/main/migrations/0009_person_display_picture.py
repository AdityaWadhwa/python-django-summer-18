# Generated by Django 2.0.7 on 2018-07-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_person_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='display_picture',
            field=models.ImageField(null=True, upload_to='dp/'),
        ),
    ]
