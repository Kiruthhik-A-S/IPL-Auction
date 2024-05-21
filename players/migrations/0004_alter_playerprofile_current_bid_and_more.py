# Generated by Django 5.0.1 on 2024-05-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_playerprofile_current_bid_playerprofile_current_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprofile',
            name='current_bid',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='current_team',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]