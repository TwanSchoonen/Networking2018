#!flask/bin/python
from flask import Blueprint
from flask import request

#from .models import *

app = Blueprint('blueprint', __name__)


@app.route("/")
def index_view():
    return "hello world"
