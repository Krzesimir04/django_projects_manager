# Generated by Django 4.0.6 on 2022-07-23 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_describtion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='dedline',
            new_name='deadline',
        ),
    ]
