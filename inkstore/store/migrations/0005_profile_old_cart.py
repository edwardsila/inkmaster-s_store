# Generated by Django 5.1.1 on 2024-09-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
