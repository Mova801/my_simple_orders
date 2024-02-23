from src.deliveryStates import DeliveryStates


class Order:
    delivery_date: str
    name: str
    surname: str
    cellphone_number: str
    order_content: str
    delivery_channel: str
    delivery_state: DeliveryStates
    payment_state: bool
    finished: bool

    def __init__(self, date: str, name: str, surname: str, cellphone_number: str, books_ordered: str,
                 delivery_channel: str, delivery_state: DeliveryStates, payment_state: bool) -> None:
        self.delivery_date = date
        self.name = name
        self.surname = surname
        self.cellphone_number = cellphone_number
        self.order_content = books_ordered
        self.delivery_channel = delivery_channel
        self.delivery_state = delivery_state
        self.payment_state = payment_state
        self.finished = False

