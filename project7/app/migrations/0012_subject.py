# Generated by Django 4.1.13 on 2024-07-09 09:41

import bson.objectid
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_standard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
    ]
