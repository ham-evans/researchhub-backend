# Generated by Django 2.2 on 2022-05-17 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0046_flag_reason_choice'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='flag',
            name='unique_flag',
        ),
    ]