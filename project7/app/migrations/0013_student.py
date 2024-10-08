# Generated by Django 4.1.13 on 2024-07-09 10:46

import bson.objectid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('roll_number', models.CharField(blank=True, max_length=20, null=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.standard')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
