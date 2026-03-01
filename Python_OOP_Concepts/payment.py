class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)
class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card.")
        print("Verifying card details and OTP...")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI.")
        print("Redirecting to UPI app for authentication...")
class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid ₹", amount, "using Wallet.")
        print("Checking wallet balance...")
def process_payment(payment_method, amount):
    payment_method.pay(amount)
credit = CreditCardPayment()
upi = UPIPayment()
wallet = WalletPayment()
print("Credit Card Payment:")
process_payment(credit, 2000)
print("\nUPI Payment:")
process_payment(upi, 1500)
print("\nWallet Payment:")
process_payment(wallet, 500)