# Generated by Django 4.2.2 on 2023-07-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]