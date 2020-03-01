# Generated by Django 2.2.10 on 2020-02-21 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0008_auto_20200113_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailrecipient',
            name='comment_subscription',
        ),
        migrations.RemoveField(
            model_name='emailrecipient',
            name='notification_frequency',
        ),
        migrations.RemoveField(
            model_name='emailrecipient',
            name='thread_subscription',
        ),
        migrations.RemoveField(
            model_name='threadsubscription',
            name='replies',
        ),
        migrations.AddField(
            model_name='commentsubscription',
            name='email_recipient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_subscription', to='mailing_list.EmailRecipient'),
        ),
        migrations.AddField(
            model_name='commentsubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
        migrations.AddField(
            model_name='threadsubscription',
            name='email_recipient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_subscription', to='mailing_list.EmailRecipient'),
        ),
        migrations.AddField(
            model_name='threadsubscription',
            name='notification_frequency',
            field=models.IntegerField(choices=[('IMMEDIATE', 0), ('DAILY', 1440), ('WEEKLY', 10080)], default=0),
        ),
        migrations.CreateModel(
            name='ReplySubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_frequency', models.IntegerField(choices=[('IMMEDIATE', 0), ('DAILY', 1440), ('WEEKLY', 10080)], default=0)),
                ('none', models.BooleanField(default=False)),
                ('replies', models.BooleanField(default=True)),
                ('email_recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_subscription', to='mailing_list.EmailRecipient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaperSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_frequency', models.IntegerField(choices=[('IMMEDIATE', 0), ('DAILY', 1440), ('WEEKLY', 10080)], default=0)),
                ('none', models.BooleanField(default=False)),
                ('threads', models.BooleanField(default=True)),
                ('email_recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paper_subscription', to='mailing_list.EmailRecipient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DigestSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_frequency', models.IntegerField(choices=[('IMMEDIATE', 0), ('DAILY', 1440), ('WEEKLY', 10080)], default=1440)),
                ('none', models.BooleanField(default=False)),
                ('email_recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digest_subscription', to='mailing_list.EmailRecipient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]