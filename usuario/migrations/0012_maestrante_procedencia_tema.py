# Generated by Django 4.2 on 2023-05-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_remove_maestrante_hora_sustentacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maestrante',
            name='procedencia_tema',
            field=models.BooleanField(default=False),
        ),
    ]