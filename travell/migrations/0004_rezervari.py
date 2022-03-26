# Generated by Django 3.1.4 on 2021-01-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_amintiri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezervari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume_locatie', models.CharField(max_length=100)),
                ('numar_persoane', models.IntegerField()),
                ('data', models.DateTimeField()),
            ],
        ),
    ]