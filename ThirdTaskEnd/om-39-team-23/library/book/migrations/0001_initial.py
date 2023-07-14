# Generated by Django 4.1 on 2022-11-21 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('name', models.CharField(blank=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('count', models.IntegerField(default=10)),
                ('year_of_publication', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('date_of_issue', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
