from flask import Flask, render_template
from src.httpMethods import HttpMethods
from src.database.db import Session, get_order

app = Flask(__name__ + ':my_simple_orders')

session = Session()


@app.route('/index/')
@app.route('/')
def index():
    orders = get_order(session)
    return render_template('index.html', orders=orders)


@app.route('/add_order/', methods=[HttpMethods.GET, HttpMethods.POST])
def add_order():
    return render_template('add_order.html')


@app.route('/on_delivery/')
def on_delivery():
    return render_template('orders_history.html')
