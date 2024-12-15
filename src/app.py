from flask import Flask, render_template
from src.httpMethods import HttpMethods

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    orders = []
    return render_template('index.html', orders=orders)


@app.get('/add_order')
def add_order():
    return render_template('add_order.html')


@app.post('/add_order')
def add_order_post():
    return render_template('add_order.html')


@app.route('/orders_history')
def orders_history():
    history = []
    return render_template('orders_history.html', orders=history)
