from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Muito obrigada por compartilhar seus conhecimento Prof Gabyy!! <3 
    "OBS: Você foi a única professora no curso, muitooo feliz em ver mulheres fodass mandando muitooo bem nesse mundão de TI! rsrs"

if __name__ == '__main__':
    app.run(debug=True)