from payment_interface import IPaymentMethod
from dataclasses import dataclass


@dataclass
class CreditCardPayment(IPaymentMethod):
    """Кредитная карта
    Args:
        IPaymentMethod (_type_): _description_
    """
    check: int

    def process_payment(self, amount):
        """
        Провести оплату c кредитки
        """
        self.check -= amount
        print(
            f"С вашей кредитной карты вычиталось {amount}$. Остаток {self.check}$")


@dataclass
class PayPalPayment(IPaymentMethod):
    """PayPal

    Args:
        IPaymentMethod (_type_): _description_
    """
    check: int

    def process_payment(self, amount):
        self.check -= amount
        print(f"С вашего PayPal вычиталось {amount}$. Остаток {self.check}$")


@dataclass
class CryptoPayment(IPaymentMethod):
    """Криптокошелек

    Args:
        IPaymentMethod (_type_): _description_
    """
    check: int

    def process_payment(self, amount):
        self.check -= amount
        print(
            f"С вашего Криптокошелька вычиталось {amount}$. Остаток {self.check}$")
