# Generated by Django 4.0 on 2022-01-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_resturant_tags_resturant_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant',
            name='natural_tag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resturant',
            name='warranty_tag',
            field=models.BooleanField(default=False),
        ),
    ]