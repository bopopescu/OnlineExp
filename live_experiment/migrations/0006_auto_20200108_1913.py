# Generated by Django 2.2.5 on 2020-01-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_experiment', '0005_auto_20200108_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionofinterest',
            name='exp',
        ),
        migrations.AddField(
            model_name='experiment',
            name='rois',
            field=models.ManyToManyField(to='live_experiment.RegionOfInterest'),
        ),
    ]