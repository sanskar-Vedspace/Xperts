# Generated by Django 5.0 on 2024-08-30 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0031_alter_cohort_end_date_alter_cohort_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cohort',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 29, 8, 34, 9, 879248, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cohort',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 29, 8, 34, 9, 879067, tzinfo=datetime.timezone.utc)),
        ),
    ]
