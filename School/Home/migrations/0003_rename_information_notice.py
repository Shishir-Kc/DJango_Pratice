# Generated by Django 5.1.4 on 2025-01-12 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_news_information'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Information',
            new_name='Notice',
        ),
    ]