from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("nutrition_deficiency_dataset.csv")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("health"))
    return render_template("login.html")

@app.route("/health", methods=["GET", "POST"])
def health():
    result = None

    if request.method == "POST":
        user_symptoms = request.form["symptoms"].lower()

        for _, row in df.iterrows():
            symptoms_list = row["symptoms"].lower().split()

            if any(symptom in user_symptoms for symptom in symptoms_list):
                result = {
                    "condition": row["condition"],
                    "deficiency_type": row["deficiency_type"],
                    "causes": row["causes"],
                    "foods": row["recommended_foods"],
                    "supplements": row["supplements"],
                    "yoga": row["yoga"],
                    "sleep": row["sleep_hours"],
                    "water": row["water_intake_liters"],
                    "risk": row["risk_level"]
                }
                break

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
