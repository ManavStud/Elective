# Generated by Django 4.2 on 2023-05-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hon_min',
            field=models.CharField(max_length=100),
        ),
    ]
