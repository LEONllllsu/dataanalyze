# Generated by Django 2.0 on 2018-05-17 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dataResource',
            new_name='task_excel_origin',
        ),
    ]