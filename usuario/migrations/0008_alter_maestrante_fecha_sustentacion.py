# Generated by Django 4.2 on 2023-05-01 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_remove_maestrante_hora_sustentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestrante',
            name='fecha_sustentacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]