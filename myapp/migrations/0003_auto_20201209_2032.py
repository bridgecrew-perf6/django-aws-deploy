# Generated by Django 2.2 on 2020-12-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201209_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libroeditorial',
            name='isbn',
            field=models.BigIntegerField(unique=True),
        ),
    ]
