# Generated by Django 4.2.5 on 2023-10-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_plans', '0002_subscriptionplan_max_streams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='max_streams',
            field=models.IntegerField(),
        ),
    ]
