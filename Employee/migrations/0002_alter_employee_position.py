# Generated by Django 5.0.2 on 2024-03-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=20),
        ),
    ]
