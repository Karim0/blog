# Generated by Django 3.0.8 on 2020-08-26 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower_recognition', '0002_flowerphoto_flower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowerphoto',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower_recognition.Flower'),
        ),
    ]
