# Generated by Django 2.0.3 on 2018-04-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybills', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basdata',
            options={'verbose_name': '基础数据'},
        ),
        migrations.AlterField(
            model_name='basdata',
            name='code',
            field=models.CharField(max_length=20, unique=True, verbose_name='编码'),
        ),
    ]