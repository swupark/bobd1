# Generated by Django 4.2.5 on 2023-11-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='food',
            new_name='menu',
        ),
    ]