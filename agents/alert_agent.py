class AlertAgent:
    def __init__(self, threshold_percent=5):
        self.threshold_percent = threshold_percent

    def check_alert(self, current_price, buy_price, symbol):
        change = ((current_price - buy_price) / buy_price) * 100

        if change >= self.threshold_percent:
            alert = f"📈 {symbol} is UP by {change:.2f}% — consider selling!"
        elif change <= -self.threshold_percent:
            alert = f"📉 {symbol} is DOWN by {change:.2f}% — consider buying more!"
        else:
            alert = f"✅ {symbol} stable — no action needed."

        return alert
    