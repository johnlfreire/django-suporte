# Generated by Django 2.2.4 on 2019-09-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suporte', '0003_auto_20190908_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
