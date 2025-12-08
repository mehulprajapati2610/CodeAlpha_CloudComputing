import psycopg2
from db_init import DATABASE_URL

def save_user(username, secret):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, secret) VALUES (%s, %s)", (username, secret))
    conn.commit()
    cur.close()
    conn.close()
