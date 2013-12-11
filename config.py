import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ansible_user:password@192.168.113.131/' + os.path.join(basedir, 'ansible_db.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')