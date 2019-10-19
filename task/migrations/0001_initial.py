# Generated by Django 2.2.6 on 2019-10-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoName', models.TextField(default='Untitled Video')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('taskType', models.CharField(choices=[('HC', 'Home Cage'), ('TV', 'Top View')], default='HC', max_length=4)),
                ('status', models.CharField(choices=[('WT', 'Waiting'), ('PR', 'Processing'), ('DE', 'Done'), ('FE', 'File Format Not Correct')], default='WT', max_length=4)),
                ('inputVideoFile', models.FileField(upload_to='inputVideos/%Y/%m/%d')),
                ('previewImage', models.ImageField(blank=True, upload_to='previewImg/%Y/%m/%d')),
                ('outputInfoFile', models.FileField(blank=True, upload_to='outputInfo/%Y/%m/%d')),
                ('outputVideoFile', models.FileField(blank=True, upload_to='outputVideo/%Y/%m/%d')),
                ('is_processing', models.BooleanField(default=False)),
                ('is_paused', models.BooleanField(default=False)),
                ('total_frames', models.IntegerField(default=-1)),
                ('processed_frames', models.IntegerField(default=0)),
            ],
        ),
    ]
