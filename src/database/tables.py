from src.database.db import db


class OrderState(db.Model):
    state = db.Column(db.String(10), primary_key=True)

    def __repr__(self):
        return f'<OrderState {self.state}>'


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    cellphone = db.Column(db.String(12))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    delivery_channel = db.Column(db.String(50), nullable=False)
    delivery_state = db.Column(db.Boolean, nullable=False)
    payment_state = db.Column(db.Boolean, nullable=False)
    state = db.Column(db.String(10), db.ForeignKey('OrderState'))

    #     order_id = Column('id', Integer, autoincrement=True, primary_key=True)
    #     customer_name = Column('customer_name', String(50))
    #     customer_surname = Column('customer_surname', String(50))
    #     customer_cellphone = Column('customer_cellphone', String(10))
    #     order_content = Column('order_content', String(100))
    #     delivery_date = Column('delivery_date', DATE)
    #     delivery_channel = Column('delivery_channel', String(50))
    #     delivery_state = Column('delivery_state', String(6), onupdate=_evaluate_delivery_state)
    #     payment_state = Column('payment_state', BOOLEAN)
    #     completion_date = Column('completion_date', DATETIME, nullable=True)
    #     order_state = relationship('order_state', ForeignKey('orderstate.state'))

# import datetime
# from sqlalchemy import Column, Integer, String, DATE, BOOLEAN, DATETIME, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
#
# from src.deliveryStates import DeliveryStates
#
# Base = declarative_base()


# class OrderState(Base):
#     __tablename__ = 'orderStates'
#     state = Column('state', String(10), primary_key=True)
#     orders = relationship("Order", back_populates="orderstate")
#
#     def __init__(self, state) -> None:
#         self.state = state
#
#
# class Order(Base):
#     __tablename__ = 'orders'
#
#     def _evaluate_delivery_state(self) -> DeliveryStates:
#         cmp = self.delivery_date >= datetime.date.today()
#         if cmp:
#             return DeliveryStates.PENDING
#         return DeliveryStates.DELAYED
#
#     order_id = Column('id', Integer, autoincrement=True, primary_key=True)
#     customer_name = Column('customer_name', String(50))
#     customer_surname = Column('customer_surname', String(50))
#     customer_cellphone = Column('customer_cellphone', String(10))
#     order_content = Column('order_content', String(100))
#     delivery_date = Column('delivery_date', DATE)
#     delivery_channel = Column('delivery_channel', String(50))
#     delivery_state = Column('delivery_state', String(6), onupdate=_evaluate_delivery_state)
#     payment_state = Column('payment_state', BOOLEAN)
#     completion_date = Column('completion_date', DATETIME, nullable=True)
#     order_state = relationship('order_state', ForeignKey('orderstate.state'))
#
#     def __init__(self, customer_name, customer_surname, customer_cellphone, order_content, delivery_date,
#                  delivery_channel, delivery_state, payment_state, order_state) -> None:
#         self.customer_name = customer_name
#         self.customer_surname = customer_surname
#         self.customer_cellphone = customer_cellphone
#         self.order_content = order_content
#         self.delivery_date = delivery_date
#         self.delivery_channel = delivery_channel
#         self.delivery_state = delivery_state
#         self.payment_state = payment_state
#         self.order_state = order_state
#
#     def __str__(self) -> str:
#         return (f'{str(self.customer_name)},{str(self.customer_surname)},{str(self.customer_cellphone)},'
#                 f'{str(self.order_content)},{str(self.delivery_date)},{str(self.delivery_channel)},'
#                 f'{str(self.delivery_state)},{str(self.payment_state)},{str(self.finished)}')
#
#     def get_date(self) -> str:
#         return datetime.date.strftime(self.delivery_date, '%d-%m-%Y')
#
#     def as_list(self) -> list:
#         return [str(self.customer_name), str(self.customer_surname), self.customer_cellphone, self.order_content,
#                 datetime.date.strftime(self.delivery_date, '%Y-%m-%d'), str(self.delivery_channel),
#                 str(self.delivery_state), self.payment_state, self.finished]
#
#     def finished_str(self) -> str:
#         if self.finished:
#             return 'CONCLUSO'
#         return 'NON CONCLUSO'
#
#     def payment_state_str(self) -> str:
#         if self.payment_state:
#             return 'PAGATO'
#         return 'DA PAGARE'
#
#     def delivery_state_str(self) -> str:
#         if self.delivery_state != DeliveryStates.DELIVERED.value:
#             self.delivery_state = self._evaluate_delivery_state()
#         return self.delivery_state
#
#     def delivery_state_color(self) -> str:
#         match self.delivery_state:
#             case DeliveryStates.DELIVERED.value:
#                 return 'green'
#             case DeliveryStates.PENDING.value:
#                 return 'orange'
#             case DeliveryStates.DELAYED.value:
#                 return 'red'
