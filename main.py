from flask import Flask, render_template
from flask_htmx import HTMX

app = Flask(__name__, template_folder='templates', static_url_path='/static')
htmx = HTMX(app)

@app.route('/')
def home():
    return render_template('index.html')
