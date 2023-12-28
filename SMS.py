#!/usr/bin/python

from flask import Flask, request, jsonify



# create flask objeck 

app = Flask(__name__)




# wirte an interface
# the full address of the interface: http://127.0.0.1:5000/sms

@app.route("/sms", methods=["POST"]
def receive():
    # get the content from the SMS forwarder
    content = request.form.get("content")
    print(content)

    return jsonify(status="ok")




if __name__ == '__main--':
    app.run()
