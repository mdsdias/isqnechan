from flask import render_template, Flask

app = Flask(__name__, template_folder="./")

@app.route("/")
def index():
    main = [
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
    return render_template('index.html', **main)

app.run('0.0.0.0', 8080, debug=True)
