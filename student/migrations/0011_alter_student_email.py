# Generated by Django 4.1.4 on 2023-05-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(db_column='email', max_length=50),
        ),
    ]
