# Generated by Django 4.1.2 on 2022-10-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='descricao',
        ),
        migrations.AddField(
            model_name='local',
            name='nome',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
