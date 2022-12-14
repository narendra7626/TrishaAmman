# Generated by Django 3.2.5 on 2022-05-10 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygoddess', '0008_auto_20220508_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrishaSlave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='trisha_slaves')),
                ('description', models.CharField(default='GoddessTrisha Slave', max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygoddess.profile')),
            ],
        ),
    ]
