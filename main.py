from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/socials")
def social():
    return render_template("social.html")

@app.route("/FAQ")
def FAQ():
    return render_template("FAQ.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)