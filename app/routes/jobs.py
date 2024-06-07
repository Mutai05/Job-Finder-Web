# app/routes/jobs.py

from flask import Blueprint, render_template
from ..models import get_db_connection

jobs_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@jobs_bp.route("/")
def jobs_archive():
    # Fetch job listings from database
    cnx = get_db_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Render the jobs archive page template with job listings data
    return render_template("jobs/jobs_archive.html", jobs=jobs)