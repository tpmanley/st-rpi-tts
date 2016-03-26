#!/usr/bin/env python
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/tts/<int:door>/open')
def open_door(door):
    print "Open %s" % door
    doors[door].open()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0') #, debug=True)

