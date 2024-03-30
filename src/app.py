from flask import Flask, render_template
from src.httpMethods import HttpMethods

app = Flask(__name__)

session = create_session()




@app.route('/index')
@app.route('/')
def index():
    orders = get_unsolved_orders(session)
    return render_template('../../books_order/templates/index.html', orders=orders)


@app.get('/add_order')
def add_order():
    return render_template('add_order.html')


@app.post('/add_order')
def add_order():
    return render_template('add_order.html')


@app.route('/orders_history')
def orders_history():
    history = get_solved_orders(session)
    return render_template('orders_history.html', orders=history)
