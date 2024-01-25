from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/shop-detail")
def shop_detail():
    return render_template("shop-detail.html")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")


@app.route("/no-found")
def no_found():
    return render_template("404.html")
