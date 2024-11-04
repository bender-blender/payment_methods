
from abc import ABC, abstractmethod


class IPaymentMethod(ABC):
    """Интерфейс платежной системы

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: _description_
    """
    @abstractmethod
    def process_payment(self, amount):
        raise NotImplementedError()
