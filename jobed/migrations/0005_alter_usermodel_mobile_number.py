# Generated by Django 5.1.2 on 2024-10-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobed', '0004_alter_usermodel_image_alter_usermodel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]