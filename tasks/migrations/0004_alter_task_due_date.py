# Generated by Django 5.2.3 on 2025-07-02 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2025, 7, 5, 17, 52, 9, 573350)),
        ),
    ]
