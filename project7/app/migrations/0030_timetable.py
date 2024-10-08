# Generated by Django 4.1.13 on 2024-07-18 10:12

import bson.objectid
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_teacherattendance_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, default=bson.objectid.ObjectId, primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('school_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.schoolclass')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.teacher')),
            ],
        ),
    ]
