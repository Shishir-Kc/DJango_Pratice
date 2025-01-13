# Generated by Django 5.1.4 on 2025-01-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('Topic', models.CharField(max_length=100)),
                ('News', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='News')),
            ],
        ),
    ]