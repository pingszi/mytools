# Generated by Django 2.0.3 on 2018-04-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybills', '0005_auto_20180409_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdebt',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, max_length=8, verbose_name='总额'),
        ),
    ]
