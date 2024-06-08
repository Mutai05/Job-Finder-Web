# app/routes/admin.py

from flask import Blueprint, render_template, request, session, redirect, url_for
from ..models import get_db_connection

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Route to render the admin login page and handle login
@admin_bp.route("/login", methods=["GET", "POST"])
def login():
    if 'logged_in' in session:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        cnx = get_db_connection()
        if cnx is None:
            return "Database connection error"

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM admin_credentials WHERE username = %s AND password = %s", (username, password))
        admin = cursor.fetchone()
        cursor.close()
        cnx.close()

        if admin:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('admin.dashboard'))
        else:
            return render_template("admin/login.html", error="Invalid credentials")

    return render_template("admin/login.html")

@admin_bp.route("/dashboard")
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('admin.login'))

    cnx = get_db_connection()
    if cnx is None:
        return "Database connection error"

    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applications")
    applications = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template("admin/dashboard.html", applications=applications)

@admin_bp.route("/logout", methods=["POST"])
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('main.home'))
