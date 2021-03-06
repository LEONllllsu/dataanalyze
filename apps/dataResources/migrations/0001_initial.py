# Generated by Django 2.0 on 2018-05-08 22:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'excel'), (2, 'txt'), (3, 'csv')], verbose_name='数据类别')),
                ('name', models.CharField(max_length=30, verbose_name='名字')),
                ('data_id', models.CharField(max_length=30, verbose_name='数据ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
        ),
    ]
