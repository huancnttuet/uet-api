import os

MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PWD = os.getenv('MYSQL_PWD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DBNAME = os.getenv('MYSQL_DBNAME')


def init_app(app):
    CLEARDB_DATABASE_URL = 'mysql://bd474dc8c06660:2c9f6312@us-cdbr-east-05.cleardb.net/heroku_e3a89c45e672a7c'
    app.config['SQLALCHEMY_DATABASE_URI'] = CLEARDB_DATABASE_URL
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
    #     MYSQL_USERNAME, MYSQL_PWD, MYSQL_HOST, MYSQL_DBNAME)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
