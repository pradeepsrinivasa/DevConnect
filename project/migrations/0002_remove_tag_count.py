# Generated by Django 5.0.7 on 2024-07-29 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='count',
        ),
    ]
