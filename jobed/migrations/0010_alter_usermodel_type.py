# Generated by Django 5.1.2 on 2024-10-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobed', '0009_remove_company_logo_company_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='type',
            field=models.CharField(blank=True, choices=[('Recruiter', 'Recruiter'), ('Student', 'Student')], max_length=50, null=True),
        ),
    ]
