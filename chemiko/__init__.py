from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kriptonavar'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask Migrate setup
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from chemiko import routes  # Make sure routes are imported after the app context is set
def create_admin():
    from chemiko.models import User  # Import the User model
    with app.app_context():  # Ensure you're within the app context
        if not User.query.filter_by(is_admin=True).first():
            hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
            admin = User(username='admin', email='admin@example.com', password=hashed_password, is_admin=True)
            db.session.add(admin)
            db.session.commit()
            print('Admin user created!')
        else:
            print('Admin user already exists.')
