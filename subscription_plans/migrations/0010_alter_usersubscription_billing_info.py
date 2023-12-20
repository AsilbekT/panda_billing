# Generated by Django 4.2.5 on 2023-10-16 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0009_alter_billinginfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscription',
            name='billing_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_info', to='subscription_plans.billinginfo'),
        ),
    ]