from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True

INSTANCE_ROUTE_PREFIX = "/instance"
MACHINE_LEARNING_ROUTE_PREFIX = "/ml"


@app.route(f"{INSTANCE_ROUTE_PREFIX}/add")
@cross_origin()
def AddInstanceEndpoint():
    return "AddInstanceEndpoint"


@app.route(f"{INSTANCE_ROUTE_PREFIX}/list")
@cross_origin()
def ListInstancesEndpoint():
    return "List Instances endpoint"


@app.route(f"{INSTANCE_ROUTE_PREFIX}/remove")
@cross_origin()
def RemoveInstanceEndpoint():
    return "Remove Instance endpoint"


@app.route(f"{MACHINE_LEARNING_ROUTE_PREFIX}/find-similar")
@cross_origin()
def FindSimilarProfilesEndpoint():
    return "FindSimilarProfilesEndpoint"


@app.route(f"{MACHINE_LEARNING_ROUTE_PREFIX}/learn")
@cross_origin()
def LearnWithCurrentInstances():
    return "LearnWithCurrentInstances"


@app.route(f"{MACHINE_LEARNING_ROUTE_PREFIX}/results")
@cross_origin()
def GetMLResultsEndpoint():
    return "GetMLResultsEndpoint"


app.run()
