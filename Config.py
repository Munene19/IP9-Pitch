# import os
#
#
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     UPLOADED_PHOTOS_DEST = 'app/static/photos'
#
#
# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:Backrow@localhost/watchlist'
#
#
# class DevConfig(Config):
#     DEBUG = True
#
#
# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig
# }
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:1234@localhost/pitch'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mike:1234@localhost/pitch'


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
