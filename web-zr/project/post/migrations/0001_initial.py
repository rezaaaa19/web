# Generated by Django 5.0.3 on 2024-04-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tizhoshan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, upload_to='', verbose_name='تصویر')),
                ('news', models.TextField(verbose_name='اخبار')),
            ],
        ),
    ]
