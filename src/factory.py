from payment_interface import IPaymentMethod
from dataclasses import dataclass


@dataclass
class Factory:
    """Фабрика

    Returns:
        _type_: _description_
    """
    way: IPaymentMethod

    def create_payment_method(self):
        """возвращает объект типа PaymentMethod

        Returns:
            _type_: _description_
        """
        return self.way
