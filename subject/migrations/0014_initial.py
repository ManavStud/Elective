# Generated by Django 4.1.5 on 2023-04-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0013_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('sub_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('dept', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=3)),
                ('hm', models.CharField(max_length=40)),
                ('sem', models.IntegerField()),
            ],
        ),
    ]