# Generated by Django 2.2.10 on 2020-02-18 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0028_auto_20200218_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='tagline',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]