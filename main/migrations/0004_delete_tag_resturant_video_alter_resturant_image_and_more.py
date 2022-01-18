# Generated by Django 4.0 on 2022-01-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_resturant_natural_tag_resturant_warranty_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='resturant',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='natural_tag',
            field=models.BooleanField(default=True),
        ),
    ]