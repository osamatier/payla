# Generated by Django 3.2 on 2022-09-14 22:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('subscribed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionAttempt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('secret_code', models.CharField(max_length=25, unique=True)),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_to', models.DateTimeField()),
                ('succeed_at', models.BooleanField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]