class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None
    SECRET_KEY = None

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'   
    SECRET_KEY = "shhh.... its very secret"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_TRACKABLE = True