# Generated by Django 4.0.5 on 2022-09-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamedesk', '0002_rename_datetime_comment_datecreation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('dd', 'ДД'), ('buyers', 'Торговцы'), ('gildmaster', 'Гилдмастеры'), ('quest', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tanner', 'Кодевники'), ('potion', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], default='tank', max_length=50),
        ),
    ]
