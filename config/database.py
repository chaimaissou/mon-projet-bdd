import mysql.connector
from mysql.connector import Error
import os

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'exam_scheduler',
    'port': 3306
}

def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erreur de connexion: {e}")
        return None

def test_connection():
    conn = get_connection()
    if conn:
        print("Connexion réussie!")
        conn.close()
        return True
    return False