# Generated by Django 4.1.5 on 2023-02-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_remove_subject_id_subject_sub_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='sub_name',
        ),
        migrations.AddField(
            model_name='subject',
            name='optional',
            field=models.BooleanField(default=False),
        ),
    ]
