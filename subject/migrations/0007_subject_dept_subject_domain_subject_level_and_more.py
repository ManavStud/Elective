# Generated by Django 4.1.5 on 2023-02-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0006_remove_subject_dept_remove_subject_domain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='dept',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='domain',
            field=models.EmailField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.CharField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='sem',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='type',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
