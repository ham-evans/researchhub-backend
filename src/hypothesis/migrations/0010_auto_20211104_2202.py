# Generated by Django 2.2 on 2021-11-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hypothesis', '0009_auto_20211104_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='type',
            field=models.CharField(choices=[('REJECT', 'REJECT'), ('SUPPORT', 'SUPPORT')], db_index=True, default='SUPPORT', help_text='Why citation was added to a hypothesis', max_length=255),
        ),
    ]