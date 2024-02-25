import datetime
from sqlalchemy import create_engine, Column, Integer, String, DATE, BOOLEAN
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import desc

from src.deliveryStates import DeliveryStates

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    def _evaluate_delivery_state(self) -> DeliveryStates:
        cmp = self.delivery_date >= datetime.date.today()
        if cmp:
            return DeliveryStates.PENDING
        return DeliveryStates.DELAYED

    order_id = Column('id', Integer, autoincrement=True, primary_key=True)
    customer_name = Column('customer_name', String(50))
    customer_surname = Column('customer_surname', String(50))
    customer_cellphone = Column('customer_cellphone', String(10))
    order_content = Column('order_content', String(100))
    delivery_date = Column('delivery_date', DATE)
    delivery_channel = Column('delivery_channel', String(50))
    delivery_state = Column('delivery_state', String(6), onupdate=_evaluate_delivery_state)
    payment_state = Column('payment_state', BOOLEAN)
    # completion_date = ???
    finished = Column('finished', BOOLEAN)

    def __init__(self, customer_name, customer_surname, customer_cellphone, order_content, delivery_date,
                 delivery_channel,
                 delivery_state, payment_state, finished) -> None:
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_cellphone = customer_cellphone
        self.order_content = order_content
        self.delivery_date = delivery_date
        self.delivery_channel = delivery_channel
        self.delivery_state = delivery_state
        self.payment_state = payment_state
        self.finished = finished

    def __str__(self) -> str:
        return (f'{str(self.customer_name)},{str(self.customer_surname)},{str(self.customer_cellphone)},'
                f'{str(self.order_content)},{str(self.delivery_date)},{str(self.delivery_channel)},'
                f'{str(self.delivery_state)},{str(self.payment_state)},{str(self.finished)}')

    def get_date(self) -> str:
        return datetime.date.strftime(self.delivery_date, '%d-%m-%Y')

    def as_list(self) -> list:
        return [str(self.customer_name), str(self.customer_surname), self.customer_cellphone, self.order_content,
                datetime.date.strftime(self.delivery_date, '%Y-%m-%d'), str(self.delivery_channel),
                str(self.delivery_state), self.payment_state, self.finished]

    def finished_str(self) -> str:
        if self.finished:
            return 'CONCLUSO'
        return 'NON CONCLUSO'

    def payment_state_str(self) -> str:
        if self.payment_state:
            return 'PAGATO'
        return 'DA PAGARE'

    def delivery_state_str(self) -> str:
        if self.delivery_state != DeliveryStates.DELIVERED.value:
            self.delivery_state = self._evaluate_delivery_state()
        return self.delivery_state

    def delivery_state_color(self) -> str:
        match self.delivery_state:
            case DeliveryStates.DELIVERED.value:
                return 'green'
            case DeliveryStates.PENDING.value:
                return 'orange'
            case DeliveryStates.DELAYED.value:
                return 'red'


def get_unsolved_orders(session) -> list[Order]:
    return (session.query(Order).filter(~Order.finished)).order_by(
        desc(Order.delivery_state)).all()


def get_solved_orders(session) -> list[Order]:
    return (session.query(Order).filter(Order.finished).order_by(
        desc(Order.delivery_state))).all()


engine = create_engine('sqlite:///database/my_orders.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
# session = Session()
#
# for _ in range(25):
#     order1 = Order('Piero', 'Pasolini', '123456789', 'I Racconti di Oscar',
#                    datetime.date(2024, 2, 23), 'Amazon', 'IN CONSEGNA', 0, 0)
#     order2 = Order('Angelo', 'Arieti', '123456654', 'Idk e Bho',
#                    datetime.date(2024, 2, 22), 'Amazon', 'IN CONSEGNA', 0, 0)
#     session.add(order1)
#     session.add(order2)
#     session.commit()
