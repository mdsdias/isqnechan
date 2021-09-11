from flask import render_template, Flask

isq = Flask(__name__)

@isq.route("/", methods=['GET'])
def index():
    main = {
        "projetos": [
            {
                "name": "GrabberTool",
                "url":"http://github.com/Isqneeh/GrabberTool",
                "desc":"Uma ferramenta feita para puxar dados de pessoas fisicas."
            },
            {
                "name": "BuscaPlacaAPI",
                "url":"http://github.com/Isqneeh/BuscaPlacaAPI",
                "desc":"Uma API POST Simples usando a biblioteca Flask; A API não contem muitos dados mais breve pretendo trazer mais"
            }
        ]
    }
    render_template('index.html', **main)

