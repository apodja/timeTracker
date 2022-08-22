# Generated by Django 4.1 on 2022-08-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To-Do'), ('ONGOING', 'Ongoing'), ('DONE', 'Done')], default='TODO', max_length=15),
        ),
    ]
