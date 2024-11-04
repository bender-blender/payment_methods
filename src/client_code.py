from payment_methods import CreditCardPayment, CryptoPayment, PayPalPayment
from payment_interface import IPaymentMethod
from factory import Factory


def client_code(way: IPaymentMethod):
    w = Factory(way(1000)).create_payment_method()
    w.process_payment(500)


lst = [CreditCardPayment, CryptoPayment, PayPalPayment]
for i in lst:
    client_code(i)
