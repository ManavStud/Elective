# Generated by Django 4.1.5 on 2023-02-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_opt_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
