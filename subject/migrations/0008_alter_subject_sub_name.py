# Generated by Django 4.1.5 on 2023-03-17 11:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0007_subject_dept_subject_domain_subject_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, null=True, size=None),
        ),
    ]