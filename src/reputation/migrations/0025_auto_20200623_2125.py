# Generated by Django 2.2.13 on 2020-06-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0024_auto_20200612_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='token_address',
            field=models.CharField(choices=[('', 'ResearchCoin address')], max_length=255),
        ),
    ]