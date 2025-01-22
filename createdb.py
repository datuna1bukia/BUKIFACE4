from chemiko import app, db
from chemiko.models import User
# Create and drop tables within the app context
with app.app_context():
    db.create_all()  # Create all tables
