# Generated by Django 5.1 on 2024-10-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/'),
        ),
    ]