# Generated by Django 5.0.7 on 2024-07-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="todo",
            name="finished_at",
            field=models.DateField(null=True),
        ),
    ]
