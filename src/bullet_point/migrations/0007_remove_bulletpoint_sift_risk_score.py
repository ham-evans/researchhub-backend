# Generated by Django 2.2 on 2020-11-14 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bullet_point', '0006_bulletpoint_sift_risk_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletpoint',
            name='sift_risk_score',
        ),
    ]