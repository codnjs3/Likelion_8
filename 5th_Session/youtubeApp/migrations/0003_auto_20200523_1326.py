# Generated by Django 3.0.6 on 2020-05-23 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeApp', '0002_auto_20200523_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='creater',
            new_name='creator',
        ),
    ]