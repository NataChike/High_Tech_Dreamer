# Generated by Django 4.1.1 on 2022-09-11 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jukus', '0002_juku_delete_zuku'),
        ('users', '0006_remove_customuser_juku_delete_juku'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='juku',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jukus.juku'),
        ),
    ]
