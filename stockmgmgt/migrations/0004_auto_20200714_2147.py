# Generated by Django 2.2 on 2020-07-14 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0003_auto_20200714_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockmgmgt.Category'),
        ),
    ]
