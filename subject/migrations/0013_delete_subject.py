# Generated by Django 4.1.5 on 2023-04-12 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0012_remove_subject_sub_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='subject',
        ),
    ]