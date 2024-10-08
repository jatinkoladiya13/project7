# Generated by Django 4.1.13 on 2024-07-13 07:05

import bson.objectid
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_schoolclass_student_school_class_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceEntery',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('attendance', djongo.models.fields.JSONField()),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
        ),
    ]
