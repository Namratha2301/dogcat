from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Code to Predict From Aud
        pass
    return render_template('home.html')
