from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
app.config['CORS_ALLOW_HEADERS'] = ["Content-Type", "Authorization"]
CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


from app import routes, model