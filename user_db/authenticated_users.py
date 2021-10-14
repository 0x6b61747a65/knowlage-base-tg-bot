import os
from aiogram.dispatcher.storage import RESULT
import psycopg2


dbname=os.getenv('DB_NAME')
username=os.getenv('DB_USERNAME')
dbpassword=os.getenv('DB_PASSWORD')
hostname=os.getenv('HOSTNAME')


conn = psycopg2.connect(dbname=dbname, user=username, password=dbpassword, host='localhost')
cur = conn.cursor()

def username_in_db_exists(username):
    cur.execute(
        "select username from users where username =%s", (username,)
    )
    result = cur.fetchone()
    if result is None:
        result = '0'
    else:
        result = result[0]
    return result

#testing connection to db
# cur.execute('select * from users')
# username = input('Username: ')
# print(username_in_db_exists(username))
