from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():

    try:
        conn = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"]
        )

        conn.close()

        return "Backend Connected To PostgreSQL"

    except Exception as e:
        return f"Database Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
