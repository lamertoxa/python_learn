# Generated by Django 4.1 on 2022-11-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'user'), (1, 'librarian'), (2, 'admin')], default=0, null=True),
        ),
    ]
