from src.app import app
from src.database.db import db

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/my_orders'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SERVER_NAME'] = 'my_simple_orders'
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=8000)
