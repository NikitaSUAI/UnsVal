# Generated by Django 4.2.7 on 2023-11-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dialogs',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='stopthemes',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
