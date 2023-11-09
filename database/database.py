import sqlite3
from config import DB_CONNECTION_STRING

def get_db_connection():
    conn = sqlite3.connect(DB_CONNECTION_STRING)
    return conn

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS validators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER NOT NULL,
            validator_address TEXT NOT NULL,
            alias TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_validator(chat_id, validator_address, alias):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO validators (chat_id, validator_address, alias) VALUES (?, ?, ?)',
                   (chat_id, validator_address, alias))
    conn.commit()
    conn.close()

def get_validators(chat_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT validator_address, alias FROM validators WHERE chat_id = ?', (chat_id,))
    validators = cursor.fetchall()
    conn.close()
    return validators

def remove_validator(chat_id, alias):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM validators WHERE chat_id = ? AND alias = ?', (chat_id, alias))
    conn.commit()
    conn.close()
