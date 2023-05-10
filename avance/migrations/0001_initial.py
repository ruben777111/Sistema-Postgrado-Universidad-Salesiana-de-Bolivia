# Generated by Django 4.2.1 on 2023-05-10 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0021_alter_maestrante_hora_sustentacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id_avance', models.AutoField(primary_key=True, serialize=False)),
                ('docente', models.CharField(blank=True, max_length=400, null=True, verbose_name='Docente')),
                ('nombre_docente', models.CharField(blank=True, max_length=400, null=True, verbose_name='Nombre docente')),
                ('fecha', models.DateField(auto_now=True, verbose_name='Fecha de registro')),
                ('actividad', models.CharField(blank=True, max_length=400, null=True, verbose_name='Actividad')),
                ('obs', models.TextField(blank=True, max_length=400, null=True, verbose_name='Observaciones')),
                ('obs_ant', models.CharField(blank=True, max_length=400, null=True, verbose_name='¿ Se mejoraron las observaciones anteriores?')),
                ('estado_avance', models.BooleanField(default=True, verbose_name='Estado')),
                ('maestrante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.maestrante')),
            ],
            options={
                'verbose_name': 'Avance',
                'verbose_name_plural': 'Avances',
            },
        ),
    ]
