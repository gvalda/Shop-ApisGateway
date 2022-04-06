from flask import Flask

from catalogue.src.catalogue.entrypoints.flask_app import crossdomain


app = Flask(__name__)


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@crossdomain(origin="*")
def catch_all(path):

    return 'OK', 200
