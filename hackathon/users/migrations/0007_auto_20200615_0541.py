# Generated by Django 2.2.12 on 2020-06-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200615_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='teamleader_username',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mastercontrol',
            name='viewing_submissions_not_allowed_message',
            field=models.CharField(default='Hold on! Viewing Submissions will be allowed at 6:00 PM', max_length=300),
        ),
        migrations.AlterField(
            model_name='mastercontrol',
            name='voting_not_allowed_message',
            field=models.CharField(default='Hold on! Voting will be allowed at 6:00 PM', max_length=300),
        ),
        migrations.AlterField(
            model_name='mastercontrol',
            name='winners_not_allowed_message',
            field=models.CharField(default='Hold on! Winners will be allowed at 6:00 PM', max_length=300),
        ),
    ]
