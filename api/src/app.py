"""
this is the main file
"""
from flask import Flask
from controllers.blueprints.calculate import CALCULATE_BP

PATH = "/v0/"

app = Flask(__name__)
app.register_blueprint(CALCULATE_BP, url_prefix=f"""{PATH}""")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    