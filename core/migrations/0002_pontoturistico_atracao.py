# Generated by Django 4.0.3 on 2022-03-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.atracao'),
        ),
    ]