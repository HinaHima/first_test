# Generated by Django 4.0.5 on 2022-07-05 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top_moments', '0002_thetop_text_thetop_top_thetop_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thetop',
            old_name='video',
            new_name='url',
        ),
    ]
