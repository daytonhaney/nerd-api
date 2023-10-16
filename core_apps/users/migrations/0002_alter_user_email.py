# Generated by Django 4.1.7 on 2023-10-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                db_index=True, max_length=150, unique=True, verbose_name="email address"
            ),
        ),
    ]
