# app/routes/main.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("main/index.html")

@main_bp.route("/about-us")
def about():
    return render_template("main/about.html")

@main_bp.route("/faqs")
def faqs():
    return render_template("main/faqs.html")

@main_bp.route("/contact-us")
def contact():
    return render_template("main/contact.html")