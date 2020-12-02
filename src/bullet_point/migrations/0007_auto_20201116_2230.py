# Generated by Django 2.2 on 2020-11-16 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bullet_point', '0006_bulletpoint_sift_risk_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('vote_type', models.IntegerField(choices=[(1, 'Upvote'), (2, 'Downvote')])),
                ('is_removed', models.BooleanField(default=False, null=True)),
                ('bulletpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', related_query_name='vote', to='bullet_point.BulletPoint')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bulletpoint_votes', related_query_name='bulletpoint_vote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('bulletpoint', 'created_by'), name='unique_bulletpoint_vote'),
        ),
    ]