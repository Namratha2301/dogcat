from flask import request, render_template
from app import app
from app.modelutils import instant_predict
from app.modelcnnutils import predict_cnn

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        aud = request.files['audio_data']
        val = instant_predict(aud)[0]
        val = 'Cat' if val == 0 else 'Dog'
        return val
    return render_template('home.html')

@app.route('/cnn', methods=['GET', 'POST'])
def home_cnn():
    if request.method == 'POST':
        aud = request.files['audio_data']
        val = predict_cnn(aud)
        val = 'Cat' if val == 0 else 'Dog'
        return val
    return render_template('home_cnn.html')
