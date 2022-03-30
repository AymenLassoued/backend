# Generated by Django 4.0.2 on 2022-03-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LIST_PIECES',
            fields=[
                ('RefOF', models.IntegerField(primary_key=True, serialize=False)),
                ('NumOF', models.IntegerField()),
                ('Qte', models.IntegerField()),
                ('Désignation', models.CharField(max_length=100)),
                ('Matiére', models.CharField(max_length=100)),
                ('Dimension', models.IntegerField()),
                ('Qual', models.CharField(max_length=100)),
                ('Prévu_h', models.IntegerField()),
                ('Réalisé_h', models.IntegerField()),
                ('Conformité_C', models.IntegerField()),
                ('Conformité_NC', models.IntegerField()),
            ],
        ),
    ]
