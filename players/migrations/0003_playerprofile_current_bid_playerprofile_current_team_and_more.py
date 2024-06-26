# Generated by Django 5.0.1 on 2024-05-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_remove_playerprofile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerprofile',
            name='current_bid',
            field=models.DecimalField(decimal_places=0, default=None, max_digits=15),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='current_team',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='playerprofile',
            name='base_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
