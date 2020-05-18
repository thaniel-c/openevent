# Generated by Django 3.0.5 on 2020-05-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200518_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, to='users.Team'),
        ),
    ]
