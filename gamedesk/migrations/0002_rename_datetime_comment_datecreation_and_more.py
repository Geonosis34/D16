# Generated by Django 4.0.5 on 2022-09-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedesk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='datetime',
            new_name='dateCreation',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(blank=True, null=True, verbose_name='Approved'),
        ),
    ]
