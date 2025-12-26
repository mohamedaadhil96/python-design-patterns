from abc import ABC, abstractmethod

# Step 1: Define an interface for payment strategies
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Step 2: Implement specific payment strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} payment using Credit Card.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} payment using PayPal.")


class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} payment using Cryptocurrency.")


# Step 3: Context class to use the strategies
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Example usage
processor = PaymentProcessor(CreditCardPayment())
processor.process_payment(100)

processor.set_strategy(PayPalPayment())
processor.process_payment(200)

processor.set_strategy(CryptoPayment())
processor.process_payment(300)
