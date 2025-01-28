from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from routes import bp as player_bp
from config import Config  


app = Flask(__name__)
app.config.from_object(Config)  # Use settings from config.py

db.init_app(app)
migrate = Migrate(app, db)

# Register routes blueprint
app.register_blueprint(player_bp)

if __name__ == "__main__":
    app.run(debug=True)
