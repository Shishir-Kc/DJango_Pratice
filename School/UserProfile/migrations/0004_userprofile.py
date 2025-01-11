# Generated by Django 5.1.4 on 2025-01-11 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_rename_userprofile_useraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bio', models.TextField(max_length=99)),
                ('profile_created_at', models.DateTimeField(auto_now_add=True)),
                ('profile_updated_at', models.DateTimeField(auto_now=True)),
                ('user_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UserProfile.useraccount')),
            ],
        ),
    ]
