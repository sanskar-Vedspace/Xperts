# Generated by Django 5.1.1 on 2024-09-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_eventregistration_payment_status_eventpayment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='event_backgrounds/'),
        ),
    ]
