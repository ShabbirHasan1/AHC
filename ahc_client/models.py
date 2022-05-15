from django.db import models


class NiftyBanknifty(models.Model):
    nifty_spot = models.FloatField(null=True)
    nifty_future = models.FloatField(null=True)
    bank_nifty_spot = models.FloatField(null=True)
    bank_nifty_future = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    loss = models.FloatField(null=True)
    mtm = models.FloatField(null=True)
    vt = models.FloatField(null=True)
    lt = models.FloatField(null=True)


class TradeStrategies(models.Model):
    strategies = models.IntegerField()
    symbol = models.IntegerField()
    expiry_date = models.DateTimeField()
    strike_price = models.FloatField()
    ce_pe_fut = models.FloatField()
    mis_nrml = models.FloatField()
    buy_sell = models.FloatField()
    order_quantity = models.IntegerField()
    partial_exit_quantity = models.IntegerField()
    target = models.FloatField()
    buy_sell_spotprice = models.FloatField()
    stop_loss = models.FloatField()
    profit_trailing = models.FloatField()
    trailing_sl_points = models.IntegerField()
    m_ma_mb = models.FloatField()
    current_sl_position = models.CharField(max_length=50)
    trade_status = models.CharField(max_length=50)
    executed_price = models.FloatField()
    live_ltp = models.FloatField()
    vwap = models.FloatField()
    mtm = models.FloatField()
    iv = models.FloatField()
    delta = models.FloatField()
    gamma = models.FloatField()
    rho = models.FloatField()
    theta = models.FloatField()
    vega = models.FloatField()
    volume = models.FloatField()
    lot_size = models.FloatField()
    capital_required_to_buy = models.FloatField()
    order_id = models.IntegerField()
    current_profit_position = models.FloatField()
    entry_time = models.DateTimeField()
    exit_time = models.DateTimeField()

    def __int__(self):
        return self.strategies
