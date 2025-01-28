import os

class Config:
    # Secret key for session management 
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')

    # Database configuration: 
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance/elite_trainer.db')}"
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask environment configuration
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
 