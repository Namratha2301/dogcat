from flask import Flask, request, render_template, url_for
from config import development, production
import os

app = Flask(__name__)

if os.environ.get('ENVIRONMENT', 'PRODUCTION').lower() == 'production':
    app.config.from_object(production)
else:
    app.config.from_object(development)

from app import routes
