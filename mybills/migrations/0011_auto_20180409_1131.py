# Generated by Django 2.0.3 on 2018-04-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybills', '0010_auto_20180409_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdebt',
            name='name',
            field=models.CharField(max_length=40, verbose_name='名称'),
        ),
    ]
