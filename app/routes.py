from flask import request, render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Code to Predict From Aud
        pass
    return render_template('home.html')
