# Generated by Django 4.2.5 on 2023-11-02 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0021_remove_transactionhistory_transaction_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionhistory',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription_plans.paymenttransaction'),
        ),
    ]
