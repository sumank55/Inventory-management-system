# Generated by Django 3.2.7 on 2021-09-28 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0013_remove_sale_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enroll.customer'),
        ),
    ]
