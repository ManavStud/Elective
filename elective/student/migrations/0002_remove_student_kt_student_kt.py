# Generated by Django 4.1.5 on 2023-02-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='kt',
        ),
        migrations.AddField(
            model_name='student',
            name='kt',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]