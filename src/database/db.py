from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy import desc

# from src.database.tables import Order, OrderState, Base


# def get_unsolved_orders(session) -> list[Order]:
#     return (session.query(Order).filter(~Order.finished)).order_by(
#         desc(Order.delivery_state)).all()
#
#
# def get_solved_orders(session) -> list[Order]:
#     return (session.query(Order).filter(Order.finished).order_by(
#         desc(Order.delivery_state))).all()
#
#
# def create_session(database_name: str) -> Session:
#     engine = create_engine(f'sqlite:///{database_name}.db', echo=True)
#     Base.metadata.create_all(bind=engine)
#     Session = sessionmaker(bind=engine)
#     return Session()
#
#
#
# session = create_session('database/my_orders')
# s1 = OrderState('NON CONCLUSO')
# s2 = OrderState('CONCLUSO')
# s3 = OrderState('CANCELLATO')
# session.add_all([s1, s2, s3])
# session.commit()
#
# for _ in range(25):
#     order1 = Order('Piero', 'Pasolini', '123456789', 'I Racconti di Oscar',
#                    datetime.date(2024, 2, 23), 'Amazon', 'IN CONSEGNA', 0, 0)
#     order2 = Order('Angelo', 'Arieti', '123456654', 'Idk e Bho',
#                    datetime.date(2024, 2, 22), 'Amazon', 'IN CONSEGNA', 0, 0)
#     session.add_all([order1,order2])
#     session.commit()

