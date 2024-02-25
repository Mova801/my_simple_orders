from flask import Flask, render_template
from src.httpMethods import HttpMethods
from src.database.db import Session, get_unsolved_orders, get_solved_orders

app = Flask(__name__ + ':my_simple_orders')

session = Session()


@app.route('/index/')
@app.route('/')
def index():
    orders = get_unsolved_orders(session)
    return render_template('index.html', orders=orders)


@app.route('/add_order/', methods=[HttpMethods.GET, HttpMethods.POST])
def add_order():
    return render_template('add_order.html')


@app.route('/orders_history/')
def orders_history():
    history = get_solved_orders(session)
    return render_template('orders_history.html', orders=history)
