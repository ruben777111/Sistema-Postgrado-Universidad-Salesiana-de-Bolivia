# Generated by Django 4.2.1 on 2023-05-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0020_maestrante_hora_sustentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestrante',
            name='hora_sustentacion',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
