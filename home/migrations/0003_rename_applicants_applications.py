# Generated by Django 5.0 on 2023-12-25 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_applicants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applicants',
            new_name='Applications',
        ),
    ]
