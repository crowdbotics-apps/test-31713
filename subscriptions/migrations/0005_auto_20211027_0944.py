# Generated by Django 2.2.24 on 2021-10-27 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20211027_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='app',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apps.App', verbose_name='App'),
        ),
    ]
