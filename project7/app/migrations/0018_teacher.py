# Generated by Django 4.1.13 on 2024-07-11 07:35

import app.models
import bson.objectid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', djongo.models.fields.ArrayField(model_container=app.models.Subject, null=True)),
                ('standard', djongo.models.fields.ArrayField(model_container=app.models.Standard, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
