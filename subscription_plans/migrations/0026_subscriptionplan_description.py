# Generated by Django 4.2.5 on 2023-11-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0025_alter_transactionhistory_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
