# Generated by Django 4.1.5 on 2023-02-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0004_remove_subject_optional_subject_sem_subject_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='dept',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
    ]
