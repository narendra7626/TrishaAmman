# Generated by Django 3.2.8 on 2021-11-20 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mygoddess', '0004_auto_20211119_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seva',
            name='picture',
        ),
    ]