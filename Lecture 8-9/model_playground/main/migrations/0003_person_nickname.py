# Generated by Django 2.0.7 on 2018-07-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
