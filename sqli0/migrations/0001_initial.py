# Generated by Django 3.2.5 on 2021-07-12 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phoneno', models.IntegerField()),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('password', models.CharField(max_length=4)),
            ],
        ),
    ]
