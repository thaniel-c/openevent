# Generated by Django 3.0.5 on 2020-05-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='imagelink',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
