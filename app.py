import pymysql.cursors
import time

while True:
    try:
        connection = pymysql.connect(host='db', user='root', password='password')
        print('WE ARE IN!', flush=True)
        break
    except:
        print('NOT YET IN.', flush=True)
        time.sleep(1)
