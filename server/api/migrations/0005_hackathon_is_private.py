# Generated by Django 4.2.1 on 2023-06-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_hackathon_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]