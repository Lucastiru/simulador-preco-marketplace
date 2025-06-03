from flask import Flask, render_template, request
from simulador import calcular_preco

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            custo = float(request.form['custo'])
            imposto = float(request.form['imposto'])
            embalagem = float(request.form['embalagem'])
            frete = float(request.form['frete'])
            comissao = float(request.form['comissao'])
            margem = float(request.form['margem'])

            resultado = calcular_preco(custo, imposto, embalagem, frete, comissao, margem)
        except:
            resultado = "Erro ao processar os valores. Verifique e tente novamente."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run()
