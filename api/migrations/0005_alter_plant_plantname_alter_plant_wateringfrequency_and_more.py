# Generated by Django 4.0.4 on 2022-05-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_plant_diseases_plant_fertilizers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='plantName',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='plant',
            name='wateringFrequency',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='plant',
            name='wateringLevel',
            field=models.TextField(default=' '),
        ),
    ]