#!/usr/bin/python3

import psycopg2
from db.config import config

conn = None
params = config()

def get_protocols():
    conn = psycopg2.connect(**params)

    cur = conn.cursor()
    cur.execute('SELECT * FROM protocolo')
    select = cur.fetchall()
    cur.close()

    if conn is not None:
        conn.close()
    
    return select