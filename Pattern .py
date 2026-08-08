# Configurable Payment Processing System
# Using Strategy Design Pattern

from abc import ABC, abstractmethod

# Abstract Strategy Class
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using Credit Card.")


# Concrete Strategy 2
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using UPI.")


# Concrete Strategy 3
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} processed using PayPal.")


# Context Class
class PaymentProcessor:

    def __init__(self):
        self.payment_method = None

    # Set the payment strategy
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    # Process payment using selected strategy
    def make_payment(self, amount):
        if self.payment_method is None:
            print("Please select a payment method.")
        else:
            self.payment_method.pay(amount)


# Main Program
processor = PaymentProcessor()

# Get payment amount
amount = float(input("Enter payment amount: ₹"))

# Display menu
print("\nSelect Payment Method")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))

# Configure strategy
if choice == 1:
    processor.set_payment_method(CreditCardPayment())

elif choice == 2:
    processor.set_payment_method(UPIPayment())

elif choice == 3:
    processor.set_payment_method(PayPalPayment())

else:
    print("Invalid choice!")
    exit()

# Make payment
processor.make_payment(amount)