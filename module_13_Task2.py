from flask import Flask
import mysql.connector
app = Flask(__name__)
def get_db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Kathmandu123'
    )
    return connection
@app.route('/airport/<icao_code>')
def get_airport(icao_code):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    if row is None:
        return {"error": "Airport not found", "ICAO": icao_code}, 404
    response = {
        "ICAO": row[0],
        "Name": row[1],
        "Location": row[2]
    }
    return response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)