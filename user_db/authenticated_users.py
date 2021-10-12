import os
import psycopg2


dbname=os.getenv('DB_NAME')
username=os.getenv('DB_USERNAME')
dbpassword=os.getenv('DB_PASSWORD')
hostname=os.getenv('HOSTNAME')


conn = psycopg2.connect(dbname=dbname, user=username, password=dbpassword, host=hostname)



conn.close()