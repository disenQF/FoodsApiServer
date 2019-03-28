import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'foods_msj',
    'charset': 'utf8'
}

db = pymysql.Connect(**config)
