from flask import Flask, request
from flask_cors import CORS, cross_origin
from ..models.models import *

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True


@app.route("/add", methods=['POST'])
@cross_origin()
def NewFeatureHandler():
    pureJSON = ...

    content_type = request.headers.get('Content-Type')
    if 'application/json' in content_type:
        json = request.json
    else:
        return 'Content-Type not supported!'
    
    data : list[AddDataRequest] = []

    return request.json


app.run()