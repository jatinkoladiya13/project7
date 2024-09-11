# Generated by Django 4.1.13 on 2024-07-24 10:56

import bson.objectid
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('exam_name', models.CharField(blank=True, max_length=255, null=True)),
                ('exam_date', models.DateField()),
                ('subjects', djongo.models.fields.JSONField()),
                ('total_mark', models.IntegerField(blank=True, null=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.standard')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
        ),
    ]
