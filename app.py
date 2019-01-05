import pymysql.cursors
import time

while True:
    try:
        connection = pymysql.connect(host='db', user='root', password='password')
        print('WE ARE IN!')
        break
    except:
        print('NOT YET IN.')
        time.sleep(1)
