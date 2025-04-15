from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import sympy as sp


app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "bluecore",
    "database": "calculator_db",
    "cursorclass": pymysql.cursors.DictCursor
}

#connect to database
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

def evaluate_expression(expression):
    try:
        result = sp.sympify(expression)
        return float(result)
    except sp.SympifyError:
        return "Invalid Expression!"

#endpoint kalkulasi
@app.route("/calculate", methods=["POST"])
def calculate():
    data =request.json
    expression = data.get("expression")

    if not expression:
        return jsonify({"error": "Try again!"}), 400

    result = evaluate_expression(expression)

    if isinstance(result, (int, float)):
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                sql = "INSERT INTO history (expression, result) VALUES (%s, %s)"
                cursor.execute(sql, (expression, result))
                conn.commit()
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()

    return jsonify({"expression": expression, "result": result})

#endpoint history
@app.route("/history", methods=["GET"])
def history():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 10")
            history = cursor.fetchall()
        return jsonify(history)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)
