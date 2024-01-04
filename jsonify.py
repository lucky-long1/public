#!/usr/bin/python

from flask import jsonify

data = {
        "name": "John",
        "age": 25
}


response = jsonify(data)
response.headers.add("Content-Type","application/json")

