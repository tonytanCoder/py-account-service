#dbtool.py
import pymysql

def connect_wxremit_db():
       return pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123456',
                           database='tan',
                           charset='latin1');