from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("california1.joblib")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        # Get values from HTML form
        med_inc = float(request.form["med_inc"])
        house_age = float(request.form["house_age"])
        ave_rooms = float(request.form["ave_rooms"])
        ave_bedrms = float(request.form["ave_bedrms"])
        population = float(request.form["population"])
        ave_occup = float(request.form["ave_occup"])
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])

        # Prepare input for model
        input_data = [[
            med_inc,
            house_age,
            ave_rooms,
            ave_bedrms,
            population,
            ave_occup,
            latitude,
            longitude
        ]]

        # Make prediction
        prediction = model.predict(input_data)[0]

        # California Housing target is in $100,000 units
        price = prediction * 100000

        # Format price
        prediction = f"${price:,.0f}"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)