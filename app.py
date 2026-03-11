from flask import Flask, render_template, redirect

app = Flask(__name__)

DISCORD = "https://discord.gg/UegEWdvk3"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order")
def order():
    return redirect(DISCORD)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)