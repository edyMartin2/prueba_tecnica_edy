"""
this is the main file
"""
from flask import Flask
app = Flask(__name__)

@app.route('/upload_batch')
def upload_batch():
    return []

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    