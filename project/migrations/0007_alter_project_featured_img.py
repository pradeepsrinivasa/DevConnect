# Generated by Django 5.0.7 on 2024-08-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_project_featured_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_img',
            field=models.ImageField(blank=True, default='../static/images/default.img', null=True, upload_to=''),
        ),
    ]
