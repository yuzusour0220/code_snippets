# Generated by Django 5.0.6 on 2024-05-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='avatars/', verbose_name='写真'),
            preserve_default=False,
        ),
    ]
