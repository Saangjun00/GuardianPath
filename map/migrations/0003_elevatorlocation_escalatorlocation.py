# Generated by Django 5.1 on 2024-09-26 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_searchhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElevatorLocation',
            fields=[
                ('SubEleExitID', models.IntegerField(primary_key=True, serialize=False)),
                ('SubEleExitKind', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'elevator_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EscalatorLocation',
            fields=[
                ('esc_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('esc_latitude', models.FloatField()),
                ('esc_longitude', models.FloatField()),
            ],
            options={
                'db_table': 'escalator_location',
                'managed': False,
            },
        ),
    ]