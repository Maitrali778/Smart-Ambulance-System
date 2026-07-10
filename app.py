from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/request")
def request():
    return render_template("request.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/patient-dashboard")
def patient_dashboard():
    return render_template("patient-dashboard.html")


@app.route("/booking-history")
def booking_history():
    return render_template("booking-history.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/admin-dashboard")
def admin_dashboard():
    return render_template("admin-dashboard.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)