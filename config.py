import os

class Config:

    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgres://gcsmktadagfavr:1951bb41d4e4c3672a19cc02df2f22e48bbdb27a56f5a0624b57cfcdc07ae0ce@ec2-3-224-97-209.compute-1.amazonaws.com:5432/df7b08ssc36k4i'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SUBJECT_PREFIX = 'Pitch-app'
    SENDER_EMAIL = 'Phoebegichuhi4@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://gcsmktadagfavr:1951bb41d4e4c3672a19cc02df2f22e48bbdb27a56f5a0624b57cfcdc07ae0ce@ec2-3-224-97-209.compute-1.amazonaws.com:5432/df7b08ssc36k4i'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://gcsmktadagfavr:1951bb41d4e4c3672a19cc02df2f22e48bbdb27a56f5a0624b57cfcdc07ae0ce@ec2-3-224-97-209.compute-1.amazonaws.com:5432/df7b08ssc36k4i'
    DEBUG = True


    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
