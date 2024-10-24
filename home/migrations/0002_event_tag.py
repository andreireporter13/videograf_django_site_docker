# Generated by Django 5.1 on 2024-10-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tag',
            field=models.CharField(choices=[('nunta', 'Nunta'), ('botez', 'Botez'), ('majorat', 'Majorat'), ('altele', 'Alte Evenimente')], default='altele', max_length=50),
        ),
    ]