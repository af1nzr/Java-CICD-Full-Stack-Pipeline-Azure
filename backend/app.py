from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Backend"

@app.route('/db')
def db_conn():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='admin',
            password='password',
            database='appdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        return f"Database time: {result[0]}"
    except Exception as e:
        return f"DB error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
