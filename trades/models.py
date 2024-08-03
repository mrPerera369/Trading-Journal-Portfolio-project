from django.db import models

class Trade(models.Model):
    TRADE_TYPES = [
        ('crypto_future', 'Crypto Future'),
        ('crypto_spot', 'Crypto Spot'),
        ('forex', 'Forex'),
    ]
    TRADE_DIRECTION_CHOICES = [
        ('Buy / Future', 'Buy / Future'),
        ('Short / Future', 'Short / Future'),
        ('Spot', 'Spot'),
    ]

    TIMEFRAME_CHOICES = [
        ('1 M', '1 Minute'),
        ('5 M', '5 Minutes'),
        ('15 M', '15 Minutes'),
        ('1 H', '1 Hour'),
        ('2 H', '2 Hours'),
        ('3 H', '3 Hours'),
        ('4 H', '4 Hours'),
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    ]

    currency_fair = models.TextField(blank=True, null=True)

    open_date = models.DateField()
    open_time = models.TimeField()
    close_date = models.DateField()
    close_time = models.TimeField()
    
    # Trade Setup fields
    trade_type = models.CharField(max_length=20, choices=TRADE_TYPES, default='crypto_spot')
    action = models.CharField(max_length=15, choices=TRADE_DIRECTION_CHOICES)  # Updated max_length to 15
    time_frame = models.CharField(max_length=10, choices=TIMEFRAME_CHOICES)
    win_lose = models.CharField(max_length=5)
    margine = models.DecimalField(max_digits=10, decimal_places=2)
    leverage = models.CharField(max_length=20)
    sl = models.CharField(max_length=20)
    tp = models.CharField(max_length=100)
    open_price = models.CharField(max_length=20)
    risk_reward_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    target_price = models.CharField(max_length=20)
    stop = models.CharField(max_length=20)
    close_price = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    gain = models.CharField(max_length=10)
    profit_loss = models.CharField(max_length=20)
    
    # Market Analysis fields
    technical_analysis_charts_patterns = models.TextField()
    technical_analysis_indicators = models.TextField()
    volume_analysis = models.TextField()
    support_resistance = models.TextField()
    trend = models.CharField(max_length=10)
    fibonacci_retracement = models.TextField()
    smc_trading = models.TextField()
    fundamental_analysis = models.TextField()
    
    # Screen Shots fields
    entry_trade_image = models.ImageField(upload_to='photos/entry/', null=True, blank=True)
    exit_trade_image = models.ImageField(upload_to='photos/exit/', null=True, blank=True)
    technical_analysis_image = models.ImageField(upload_to='photos/technical/', null=True, blank=True)
    
    # Mistakes fields
    mistakes = models.JSONField(default=list, blank=True, null=True)
    
    # Lessons Learned fields
    lessons = models.JSONField(default=list, blank=True, null=True)
    
    # Additional fields
    additional = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return f"Trade {self.id} - {self.open_date} - {self.open_time} - {self.currency_fair}"
