# app/routes/jobs.py

from flask import Blueprint, render_template

jobs_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@jobs_bp.route("/")
def jobs_archive():
    return render_template("jobs/jobs_archive.html")