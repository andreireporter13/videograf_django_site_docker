# Generated by Django 5.1 on 2024-10-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_review_email_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='role',
            field=models.CharField(choices=[('client', 'Client'), ('coleg', 'Coleg')], default='client', max_length=10),
        ),
    ]