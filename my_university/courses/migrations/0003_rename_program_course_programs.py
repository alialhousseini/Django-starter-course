# Generated by Django 4.2.4 on 2023-08-07 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_program_course_program'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='program',
            new_name='programs',
        ),
    ]
