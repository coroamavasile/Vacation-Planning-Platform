# Generated by Django 3.1.4 on 2021-01-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='nume_locatie',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
