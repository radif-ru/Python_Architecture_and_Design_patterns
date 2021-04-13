# Generated by Django 3.0.7 on 2020-07-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('repaid_len', models.PositiveIntegerField(default=1, verbose_name='длительность ремонта в днях')),
            ],
        ),
        migrations.AlterField(
            model_name='repair',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repairapp.Phone', verbose_name='Смартфон'),
        ),
    ]
