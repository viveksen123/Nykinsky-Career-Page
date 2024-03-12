# Generated by Django 5.0 on 2023-12-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('current_company', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('websites', models.CharField(max_length=255)),
                ('info', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'application_forms',
            },
        ),
    ]
