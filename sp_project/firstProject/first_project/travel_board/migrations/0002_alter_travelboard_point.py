# Generated by Django 5.0.6 on 2024-06-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travel_board", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="travelboard",
            name="point",
            field=models.IntegerField(
                choices=[
                    (0, "ZERO"),
                    (1, "ONE"),
                    (2, "TWO"),
                    (3, "THREE"),
                    (4, "FOUR"),
                    (5, "FIVE"),
                ],
                default=0,
            ),
        ),
    ]
