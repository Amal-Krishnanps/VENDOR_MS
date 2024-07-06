# Generated by Django 5.0.6 on 2024-07-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendors", "0007_alter_historicalperformance_average_response_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalperformance",
            name="average_response_time",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="fullfillment_rate",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="on_time_delivery_rate",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="historicalperformance",
            name="quality_rating_avg",
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="quality_rating",
            field=models.FloatField(default=0, null=True),
        ),
    ]
