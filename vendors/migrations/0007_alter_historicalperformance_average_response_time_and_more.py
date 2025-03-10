# Generated by Django 5.0.6 on 2024-07-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendors", "0006_alter_historicalperformance_average_response_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="average_response_time",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="fullfillment_rate",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="on_time_delivery_rate",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="quality_rating_avg",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
