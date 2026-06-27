print("El programa empezó")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    print("Iniciando servidor...")
    app.run(debug=True)