# Generated by Django 4.2 on 2023-04-12 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_service', '0003_rename_starttime_showtimes_start_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='cineme',
            new_name='cinema',
        ),
        migrations.DeleteModel(
            name='ShowTimes',
        ),
    ]