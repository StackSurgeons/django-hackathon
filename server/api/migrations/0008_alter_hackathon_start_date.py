# Generated by Django 4.2.2 on 2023-07-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_hackathon_participants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='start_date',
            field=models.DateField(),
        ),
    ]