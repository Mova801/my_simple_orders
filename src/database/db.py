import datetime

from sqlalchemy import create_engine, Column, Integer, String, DATE, BOOLEAN
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import desc

Base = declarative_base()


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column('id', Integer, autoincrement=True, primary_key=True)
    client_name = Column('client_name', String(50))
    client_surname = Column('client_surname', String(50))
    client_cellphone = Column('client_cellphone', String(10))
    order_content = Column('order_content', String(100))
    delivery_date = Column('delivery_date', DATE)
    delivery_channel = Column('delivery_channel', String(50))
    delivery_state = Column('delivery_state', String(6))
    payment_state = Column('payment_state', BOOLEAN)
    finished = Column('finished', BOOLEAN)

    def __init__(self, client_name, client_surname, client_cellphone, order_content, delivery_date, delivery_channel,
                 delivery_state, payment_state, finished) -> None:
        self.client_name = client_name
        self.client_surname = client_surname
        self.client_cellphone = client_cellphone
        self.order_content = order_content
        self.delivery_date = delivery_date
        self.delivery_channel = delivery_channel
        self.delivery_state = delivery_state
        self.payment_state = payment_state
        self.finished = finished

    def __str__(self) -> str:
        return (f'{str(self.client_name)},{str(self.client_surname)},{str(self.client_cellphone)},'
                f'{str(self.order_content)},{str(self.delivery_date)},{str(self.delivery_channel)},'
                f'{str(self.delivery_state)},{str(self.payment_state)},{str(self.finished)}')

    def as_list(self) -> list:
        return [str(self.client_name), str(self.client_surname), self.client_cellphone, self.order_content,
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

    def delivery_state_color(self) -> str:
        match self.delivery_state:
            case 'CONSEGNATO':
                return 'green'
            case 'IN CONSEGNA':
                return 'orange'
            case 'IN RITARDO':
                return 'red'


def get_order(session) -> list[Order]:
    return session.query(Order).order_by(desc(Order.delivery_state)).all()


engine = create_engine('sqlite:///database/my_orders.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
# session = Session()
#
# order1 = Order('Piero', 'Pasolini', '123456789', 'I Racconti di Oscar',
#                datetime.date(2024, 2, 23), 'Amazon', 'IN CONSEGNA', 0, 0)
# order2 = Order('Angelo', 'Arieti', '123456654', 'Idk e Bho',
#                datetime.date(2024, 2, 22), 'Amazon', 'IN CONSEGNA', 0, 0)
# session.add(order1)
# session.add(order2)
# session.commit()
#
# orders = session.query(Order).all()
# for order in orders:
#     print(order.order_content)
