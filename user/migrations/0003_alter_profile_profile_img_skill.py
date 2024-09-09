# Generated by Django 5.0.7 on 2024-08-05 10:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='profiles/'),
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('descrptiion', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
