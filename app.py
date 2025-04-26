from flask import Flask, render_template
from flask_minify import Minify
from datetime import datetime, date, timedelta
import os
from flask import Flask, render_template
from flask_cors import CORS
from includes.models import db_session, init_db
from includes.api import api_bp
from includes.auth import auth_bp
from itsdangerous.url_safe import URLSafeSerializer
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["FLASK_ENV"] = os.environ.get('FLASK_ENV', "development")
if app.config["FLASK_ENV"] == "production":
    Minify(app=app, html=True, js=True, cssless=True)
app.config["TEMPLATES_AUTO_RELOAD"] = os.environ.get('TEMPLATES_AUTO_RELOAD',False)
app.config["BASE_URL_APP"] = os.environ.get('BASE_URL_APP','http://127.0.0.1:5000/')
app.config["BASE_URL_CDN"] = os.environ.get('BASE_URL_CDN','http://127.0.0.1:5000/static/')


# Secret key (placeholder)
app.secret_key = os.getenv("SECRET_KEY", "change-me-please")

# Initialize SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data.db")
init_db(DATABASE_URL)

# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

# Cleanup
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    app.run(debug=True)