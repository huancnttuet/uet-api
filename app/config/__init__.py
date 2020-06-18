import os

MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PWD = os.getenv('MYSQL_PWD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_DBNAME = os.getenv('MYSQL_DBNAME')


def init_app(app):
    print(MYSQL_HOST)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        MYSQL_USERNAME, MYSQL_PWD, MYSQL_HOST, MYSQL_DBNAME)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
