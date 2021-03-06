# Generated by Django 2.2.13 on 2020-06-21 13:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_moviex'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Moviex',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='movies',
            name='overview',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='poster_path',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
