# Generated by Django 5.0.6 on 2024-07-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField()),
                ('open_time', models.TimeField()),
                ('close_date', models.DateField()),
                ('close_time', models.TimeField()),
                ('trade_type', models.CharField(choices=[('crypto_future', 'Crypto Future'), ('crypto_spot', 'Crypto Spot'), ('forex', 'Forex')], default='crypto_spot', max_length=20)),
                ('action', models.CharField(choices=[('Buy / Future', 'Buy / Future'), ('Short / Future', 'Short / Future'), ('Spot', 'Spot')], max_length=15)),
                ('time_frame', models.CharField(choices=[('1 M', '1 Minute'), ('5 M', '5 Minutes'), ('15 M', '15 Minutes'), ('1 H', '1 Hour'), ('2 H', '2 Hours'), ('3 H', '3 Hours'), ('4 H', '4 Hours'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], max_length=10)),
                ('win_lose', models.CharField(max_length=5)),
                ('margine', models.DecimalField(decimal_places=2, max_digits=10)),
                ('leverage', models.CharField(max_length=20)),
                ('sl', models.CharField(max_length=20)),
                ('tp', models.CharField(max_length=100)),
                ('open_price', models.CharField(max_length=20)),
                ('risk_reward_ratio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('target_price', models.CharField(max_length=20)),
                ('stop', models.CharField(max_length=20)),
                ('close_price', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
                ('gain', models.CharField(max_length=10)),
                ('profit_loss', models.CharField(max_length=20)),
                ('technical_analysis_charts_patterns', models.TextField()),
                ('technical_analysis_indicators', models.TextField()),
                ('volume_analysis', models.TextField()),
                ('support_resistance', models.TextField()),
                ('trend', models.CharField(max_length=10)),
                ('fibonacci_retracement', models.TextField()),
                ('smc_trading', models.TextField()),
                ('fundamental_analysis', models.TextField()),
                ('entry_trade_image', models.ImageField(blank=True, null=True, upload_to='photos/entry/')),
                ('exit_trade_image', models.ImageField(blank=True, null=True, upload_to='photos/exit/')),
                ('technical_analysis_image', models.ImageField(blank=True, null=True, upload_to='photos/technical/')),
                ('mistakes', models.JSONField(blank=True, default=list, null=True)),
                ('lessons', models.JSONField(blank=True, default=list, null=True)),
                ('additional', models.JSONField(blank=True, default=list, null=True)),
            ],
        ),
    ]
