# Generated by Django 5.0.6 on 2024-06-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TravelBoard",
            fields=[
                ("boardId", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=128)),
                ("writer", models.CharField(max_length=32)),
                (
                    "point",
                    models.CharField(
                        choices=[
                            ("0.00", "ZERO"),
                            ("1.00", "ONE"),
                            ("2.00", "TWO"),
                            ("3.00", "THREE"),
                            ("4.00", "FOUR"),
                            ("5.00", "FIVE"),
                        ],
                        default="0.00",
                        max_length=4,
                    ),
                ),
                ("review", models.TextField()),
                ("regDate", models.DateTimeField(auto_now_add=True)),
                ("updDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "travel_board",
            },
        ),
    ]
