# Generated by Django 4.1 on 2022-08-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_entry_stop_alter_entry_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
