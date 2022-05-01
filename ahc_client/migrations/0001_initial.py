# Generated by Django 4.0.4 on 2022-04-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NiftyBanknifty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nifty_spot', models.FloatField()),
                ('nifty_future', models.FloatField()),
                ('nifty_profit', models.FloatField()),
                ('nifty_loss', models.FloatField()),
                ('nifty_MTM', models.FloatField()),
                ('nifty_LV', models.FloatField()),
                ('nifty_PV', models.FloatField()),
                ('banknifty_spot', models.FloatField()),
                ('banknifty_future', models.FloatField()),
                ('banknifty_profit', models.FloatField()),
                ('banknifty_loss', models.FloatField()),
                ('banknifty_MTM', models.FloatField()),
                ('banknifty_LV', models.FloatField()),
                ('banknifty_PV', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TradeStrategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategies', models.IntegerField()),
                ('symbol', models.IntegerField()),
                ('expiry_date', models.DateTimeField()),
                ('strike_price', models.FloatField()),
                ('ce_pe_fut', models.FloatField()),
                ('mis_nrml', models.FloatField()),
                ('buy_sell', models.FloatField()),
                ('order_quantity', models.IntegerField()),
                ('partial_exit_quantity', models.IntegerField()),
                ('target', models.FloatField()),
                ('buy_sell_spotprice', models.FloatField()),
                ('stop_loss', models.FloatField()),
                ('profit_trailing', models.FloatField()),
                ('trailing_sl_points', models.IntegerField()),
                ('m_ma_mb', models.FloatField()),
                ('current_sl_position', models.CharField(max_length=50)),
                ('trade_status', models.CharField(max_length=50)),
                ('executed_price', models.FloatField()),
                ('live_ltp', models.FloatField()),
                ('vwap', models.FloatField()),
                ('mtm', models.FloatField()),
                ('iv', models.FloatField()),
                ('delta', models.FloatField()),
                ('gamma', models.FloatField()),
                ('rho', models.FloatField()),
                ('theta', models.FloatField()),
                ('vega', models.FloatField()),
                ('volume', models.FloatField()),
                ('lot_size', models.FloatField()),
                ('capital_required_to_buy', models.FloatField()),
                ('order_id', models.IntegerField()),
                ('current_profit_position', models.FloatField()),
                ('entry_time', models.DateTimeField()),
                ('exit_time', models.DateTimeField()),
            ],
        ),
    ]
