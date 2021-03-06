import os




class Config:

    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLAlCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Atara@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):

     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)

       
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Atara@localhost/blog_test'
    



class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Atara@localhost/blog'
    
    DEBUG = True



config_options = {
    "production": ProdConfig,
    "development": DevConfig,
    "test":TestConfig
} 