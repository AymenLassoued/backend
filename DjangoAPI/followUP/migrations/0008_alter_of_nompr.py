# Generated by Django 4.0.2 on 2022-03-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followUP', '0007_alter_of_nompr_alter_of_numof_alter_of_priorité_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='of',
            name='NomPr',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
