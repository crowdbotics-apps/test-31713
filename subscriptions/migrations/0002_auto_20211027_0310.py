# Generated by Django 2.2.24 on 2021-10-27 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set(),
        ),
    ]
