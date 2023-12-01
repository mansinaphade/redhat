from flask import Flask
import os

app = Flask(_name_)

@app.route('/')
def hello():
    return "Hello World!"

if _name_ == '_main_':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
