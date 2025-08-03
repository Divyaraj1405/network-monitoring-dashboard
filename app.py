from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/logs')
def get_logs():
    df = pd.read_csv('logs.csv')
    grouped = df['protocol'].value_counts().to_dict()
    return jsonify(grouped)

if __name__ == '__main__':
    app.run(debug=True)