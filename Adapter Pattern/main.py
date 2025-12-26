# Adaptee: The old class with a different method
class BankService:
    def make_payment(self, amount):
        print(f"Processing payment of ${amount} through BankService")


# Interface
class PaymentService:
    def pay(self, amount):
        pass


# Adapter
class BankServiceAdapter(PaymentService):
    def __init__(self, bank_service: BankService):
        self.bank_service = bank_service

    def pay(self, amount):
        self.bank_service.make_payment(amount)


# Client Code: Expects a 'pay(amount)' method
def process_payment(payment_service, amount):
    payment_service.pay(amount)


# Attempt to use the BankServiceAdapter
bank_service_adapter = BankServiceAdapter(BankService())
process_payment(bank_service_adapter, 100)
