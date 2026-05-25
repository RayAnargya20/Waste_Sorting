from flask import Flask, render_template, request
from logic import classify_waste
from database import init_db, insert_data

app = Flask(__name__)

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form["waste"]

        category, recommendation = classify_waste(user_input)

        insert_data(user_input, category, recommendation)

        result = {
            "input": user_input,
            "category": category,
            "recommendation": recommendation
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)