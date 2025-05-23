# Generated by Django 5.2 on 2025-04-23 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_time', '0003_alter_movie_movie_trailer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ManyToManyField(related_name='director_names', to='movie_time.movie'),
        ),
        migrations.AlterField(
            model_name='movielanguages',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_videos', to='movie_time.movie'),
        ),
        migrations.AlterField(
            model_name='moviemoments',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_moments', to='movie_time.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='movie_time.movie'),
        ),
    ]
