# deepbook.py


class DeepPrice:
    def __init__(self, price, timestamp):
        self.price = price
        self.timestamp = timestamp

    def __str__(self):
        return f"Price: {self.price}, Timestamp: {self.timestamp}"

def add_price_point(price, timestamp):
    new_price = DeepPrice(price, timestamp)
    print(new_price)
