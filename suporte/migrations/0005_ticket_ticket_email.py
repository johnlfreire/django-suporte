# Generated by Django 2.2.4 on 2019-09-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suporte', '0004_ticket_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
