# Generated by Django 3.1.3 on 2022-01-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_svc', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='discountcode',
            index=models.Index(fields=['status'], name='discount_sv_status_0d3be2_idx'),
        ),
        migrations.AddIndex(
            model_name='discountcode',
            index=models.Index(fields=['campaign_id'], name='discount_sv_campaig_eb1c1c_idx'),
        ),
    ]
