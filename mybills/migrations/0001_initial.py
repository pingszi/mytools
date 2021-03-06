# Generated by Django 2.0.3 on 2018-04-09 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('code', models.CharField(max_length=20, verbose_name='编码')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('parent_id', models.IntegerField(default=-1, verbose_name='父编号')),
                ('add_who', models.IntegerField(verbose_name='添加人')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('edit_who', models.IntegerField(blank=True, null=True, verbose_name='编辑人')),
                ('edit_time', models.DateField(auto_now=True, verbose_name='编辑时间')),
            ],
            options={
                'db_table': 'bill_bas_data',
                'verbose_name': '基础数据管理',
            },
        ),
    ]
