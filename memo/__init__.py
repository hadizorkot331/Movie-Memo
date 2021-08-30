from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = 'super secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///memo.sql'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(user_id):
    from memo.models import User
    return User.query.get(user_id)