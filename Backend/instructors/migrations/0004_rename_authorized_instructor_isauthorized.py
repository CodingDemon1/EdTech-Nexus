# Generated by Django 4.2.4 on 2023-09-05 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0003_instructor_authorized'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='authorized',
            new_name='isAuthorized',
        ),
    ]
