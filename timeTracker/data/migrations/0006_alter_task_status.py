# Generated by Django 4.1 on 2022-08-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_entry_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('TODO', 'To-Do'), ('ONGOING', 'Ongoing'), ('DONE', 'Done')], default='TODO', max_length=15, null=True),
        ),
    ]
