# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:42:40 2022

@author: rache
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

