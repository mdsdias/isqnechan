from flask import render_template, Flask

isq = Flask(__name__)

@isq.route('/')
def __init__():
    load = {
        "pro": [
            {"name": "GrabberTool", 
             "url":"http://github.com/Isqneeh/GrabberTool",
             "desc":"Uma ferramenta feita para puxar dados de pessoas fisicas."
             }
        ]
    }
    render_template('index.html', **load)