print("El programa empezó")

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "alianzalima"

USUARIO = "admin"
PASSWORD = "1234"
CLAVE_ADMIN = "alianzavnicotetra"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == USUARIO and password == PASSWORD:

            session["usuario"] = "Administrador"
            session["estado"] = "Sesión iniciada"

            return redirect(url_for("dashboard"))

        else:

            return render_template(
                "login.html",
                error="Usuario o contraseña incorrectos"
            )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        usuario=session["usuario"],
        estado=session["estado"]
    )
@app.route("/admin", methods=["GET", "POST"])
def admin():

    if "usuario" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        clave = request.form["clave"]

        if clave == CLAVE_ADMIN:
            return render_template("admin.html")

        return render_template(
            "admin_login.html",
            error="Contraseña incorrecta"
        )

    return render_template("admin_login.html")

if __name__ == "__main__":
    print("Iniciando servidor...")
    app.run(debug=True)