# Generated by Django 4.2.2 on 2023-06-16 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('music_file', models.FileField(upload_to='music/')),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('protected', 'Protected')], default='public', max_length=10)),
                ('allowed_users', models.ManyToManyField(blank=True, related_name='allowed_files', to=settings.AUTH_USER_MODEL)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
