from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "FIAP 7ASO - Fase 5 - Luciano Carmo"

if __name__ == '__main__':
    app.run()