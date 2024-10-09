# Generated by Django 5.1.1 on 2024-09-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavigationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_logo', models.ImageField(help_text='Upload logo for the normal header.', upload_to='logos/')),
                ('sticky_logo', models.ImageField(help_text='Upload logo for the sticky header.', upload_to='logos/')),
            ],
        ),
    ]
