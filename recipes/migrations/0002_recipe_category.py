# Generated by Django 4.2.7 on 2023-11-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="category",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
