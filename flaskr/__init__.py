import os

from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # TODO: sostituire on valore random per il deployment
        DATABASE=os.path.join(app.instance_path, 'orders.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # pages
    @app.get('/index')
    def index() -> str:
        orders = []
        return render_template('index.html', orders=orders)

    @app.post('/index')
    def index_post() -> str:
        return '<h1>INDEX POST!</h1>'

    @app.get('/new_order')
    def add_order() -> str:
        return render_template('add_order.html')

    @app.post('/new_order')
    def add_order() -> str:
        return '<h1>INDEX POST!</h1>'

    @app.get('/history')
    def orders_history() -> str:
        history = []
        return render_template('orders_history.html', orders=history)

    @app.post('/history')
    def orders_history() -> str:
        return '<h1>INDEX POST!</h1>'

    return app
