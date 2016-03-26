#!/usr/bin/env python
import subprocess
from flask import Flask, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Volume(Resource):
    def get(self):
        return subprocess.check_output("amixer get PCM|grep -o [0-9]*%|sed 's/%//'", shell=True).strip()

#    def put(self, vol):
#        subprocess.call("sudo amixer set PCM -- %s" % vol, shell=True)

api.add_resource(Volume, '/speaker/volume')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

