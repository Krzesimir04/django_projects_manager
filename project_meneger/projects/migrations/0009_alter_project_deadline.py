# Generated by Django 4.0.6 on 2022-07-26 09:38

from django.db import migrations, models
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(blank=True, null=True, validators=[projects.validators.validate_deadline]),
        ),
    ]
