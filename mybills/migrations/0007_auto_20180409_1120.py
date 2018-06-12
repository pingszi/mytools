# Generated by Django 2.0.3 on 2018-04-09 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybills', '0006_auto_20180409_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basdata',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='basdata',
            name='type_desc',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='类型描述'),
        ),
        migrations.AlterField(
            model_name='busdebt',
            name='status',
            field=models.ForeignKey(limit_choices_to={'type': 'DEBT_STATUS'}, on_delete=django.db.models.deletion.CASCADE, to='mybills.BasData', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='busdebt',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='总额'),
        ),
    ]