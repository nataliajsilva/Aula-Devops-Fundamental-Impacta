from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "teste4"

if __name__ == '__main__':
    app.run(debug=True)