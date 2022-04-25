import requests
from flask import Flask, Response, request

from gateway.utils.cors_handler import crossdomain
from gateway.config import paths
from gateway.enums import StatusCodes

app = Flask(__name__)


# TODO Create authorization
# TODO Escape from ASCII symbols in request.data

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@crossdomain(origin="*")
def catch_all(path):
    for path_lib, url in paths.items():
        if(path.startswith(path_lib)):
            if(request.method == 'GET'):
                resp = requests.get(f'{url}/{path}')
            elif(request.method == 'POST'):
                resp = requests.post(f'{url}/{path}', json=request.get_json())
            else:
                return 'Not allowed', StatusCodes.METHOD_NOT_ALLOWED_405
            response = Response(
                resp.content, resp.status_code)
            return response
    return 'Not Found', StatusCodes.NOT_FOUND_404
