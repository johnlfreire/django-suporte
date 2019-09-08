# Generated by Django 2.0.7 on 2019-09-07 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_text', models.CharField(max_length=200)),
                ('autor_text', models.CharField(max_length=200)),
                ('conteudo_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_text', models.CharField(max_length=200)),
                ('descricao_text', models.CharField(max_length=200)),
                ('prioridade_text', models.CharField(max_length=200)),
                ('departamento_text', models.CharField(max_length=200)),
                ('autor_text', models.CharField(max_length=200)),
                ('chamados_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='dialogo',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suporte.Ticket'),
        ),
    ]