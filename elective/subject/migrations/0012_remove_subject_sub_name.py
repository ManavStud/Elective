# Generated by Django 4.1.5 on 2023-04-12 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0011_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='sub_name',
        ),
    ]