from flask import Flask, render_template, request, redirect, session
from karar import karar_ver

app = Flask(__name__)
app.secret_key = "karar-asistani"

# Demo kullanıcı
USER = "admin"
PASS = "1234"

gecmis = []


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER and password == PASS:
            session["user"] = username
            return redirect("/")

        return render_template(
            "login.html",
            hata="❌ Kullanıcı adı veya şifre yanlış"
        )

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/", methods=["GET", "POST"])
def index():

    if "user" not in session:
        return redirect("/login")

    cevap = None

    if request.method == "POST":
        soru = request.form["soru"]
        cevap = karar_ver(soru)

        gecmis.append({
            "soru": soru,
            "cevap": cevap
        })

    return render_template("index.html", cevap=cevap)


@app.route("/gecmis")
def gecmis_sayfasi():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "gecmis.html",
        gecmis=gecmis
    )


if __name__ == "__main__":
    app.run(debug=True)