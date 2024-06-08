# app/routes/jobs.py

from flask import Blueprint, render_template, request, abort
from ..models import get_db_connection
import mysql.connector

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


@jobs_bp.route("/<int:id>")
def jobs_item(id):
    # Fetch the specific job item from the database
    cnx = get_db_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))
    job = cursor.fetchone()
    cursor.close()
    cnx.close()

    if not job:
        abort(404)

    # Render the jobs archive page template with job listings data
    return render_template("jobs/job_item.html", job=job)

@jobs_bp.route("/apply-job", methods=['GET', 'POST'])
def apply_job():
    # Handle both GET and POST requests for the apply job page
    if request.method == "POST":
        # Handle form submission
        details = request.form
        full_name = details['full_name']
        email = details['email']
        linkedin_url = details['linkedin_url']
        education = details['education']
        work_experience = details['work_experience']
        resume_url = details['resume_url']
        cnx = get_db_connection()
        if cnx is None:
            return "Database connection error"
        cursor = cnx.cursor()
        try:
            cursor.execute("INSERT INTO applications (full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (%s, %s, %s, %s, %s, %s)", 
               (full_name, email, linkedin_url, education, work_experience, resume_url))

            cnx.commit()
            # Render a success template with submitted details
            return render_template("jobs/application_success.html", full_name=full_name, email=email, linkedin_url=linkedin_url, education=education, work_experience=work_experience, resume_url=resume_url)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 'error'
        finally:
            cursor.close()
            cnx.close()
    else:
        # Render the apply job page template for GET requests
        return render_template("jobs/apply_job.html")
    