# Generated by Django 5.0.3 on 2024-03-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='f28a11', max_length=6),
        ),
    ]
