# run.py

from app import jobfinder_web

app = jobfinder_web()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)