# Generated by Django 5.0.3 on 2024-03-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0010_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='ba991d', max_length=6),
        ),
    ]
