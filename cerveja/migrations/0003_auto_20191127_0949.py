# Generated by Django 2.2.7 on 2019-11-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerveja', '0002_auto_20191127_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cervejas',
            name='fabric',
            field=models.DateField(auto_now=True, verbose_name='Fabricação'),
        ),
    ]