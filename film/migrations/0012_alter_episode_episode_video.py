# Generated by Django 3.2.7 on 2021-10-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0011_alter_movies_movie_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='episode_video',
            field=models.FileField(upload_to='s_videos'),
        ),
    ]