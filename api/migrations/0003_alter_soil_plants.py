# Generated by Django 4.0.4 on 2022-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_plants_plant_rename_soils_soil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='plants',
            field=models.ManyToManyField(related_name='plants', to='api.plant'),
        ),
    ]
