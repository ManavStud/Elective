# Generated by Django 4.1.5 on 2023-02-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_kt_student_kt'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admit_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
