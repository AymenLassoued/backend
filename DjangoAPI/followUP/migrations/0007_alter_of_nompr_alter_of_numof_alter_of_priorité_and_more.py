# Generated by Django 4.0.2 on 2022-03-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followUP', '0006_alter_of_nompr_alter_of_numof_alter_of_priorité_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='of',
            name='NomPr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='of',
            name='NumOF',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='of',
            name='Priorité',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='of',
            name='StatutPr',
            field=models.CharField(default='', max_length=100),
        ),
    ]
