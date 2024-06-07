# app/routes/main.py

from flask import Blueprint, render_template
from ..models import get_db_connection

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    # Fetch job listings from database
    cnx = get_db_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT id, title, location, salary, currency FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    cnx.close()
    return render_template("main/index.html", jobs=jobs)

@main_bp.route("/about-us")
def about():
    return render_template("main/about.html")

@main_bp.route("/faqs")
def faqs():
    return render_template("main/faqs.html")

@main_bp.route("/contact-us")
def contact():
    return render_template("main/contact.html")