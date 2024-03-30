# Generated by Django 5.0.3 on 2024-03-28 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('episodes', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnimeCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_type', models.CharField(choices=[('want_to_watch', '想看'), ('watched', '看过'), ('watching', '在看'), ('on_hold', '搁置'), ('dropped', '抛弃')], max_length=20)),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(blank=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.anime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
