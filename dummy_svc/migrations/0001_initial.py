# Generated by Django 3.1.3 on 2022-01-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Available to use'), ('U', 'Already Used')], default='A', max_length=1)),
                ('brand_id', models.IntegerField()),
                ('customer_id', models.IntegerField(null=True)),
                ('campaign_id', models.IntegerField()),
                ('discount_type', models.CharField(choices=[('F', 'Fixed Amount Discount'), ('P', 'Percentile Discount')], max_length=1)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('expire_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
