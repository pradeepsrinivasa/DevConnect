# Generated by Django 5.0.7 on 2024-09-03 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_alter_project_featured_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_img',
            field=models.ImageField(blank=True, default=ValueError, null=True, upload_to=''),
        ),
    ]
