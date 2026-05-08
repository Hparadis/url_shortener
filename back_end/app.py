from routes.url_shortner import url_shortner_bp,route_bp
from flask import Flask 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from services.db import db
app = Flask(__name__)
CORS(app)

# our routes registers
app.register_blueprint(url_shortner_bp,url_prefix='/shorten')
app.register_blueprint(route_bp)    

# our sql database configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)