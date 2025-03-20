from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        n3 = float(request.form['n3'])
        n4 = float(request.form['n4'])

        NG = n1 + n2 + n3 + n4
        M = NG / 4

        if M >= 20:
            resultado = f"O aluno foi aprovado com {M:.2f} pontos na média anual."
        else:
            resultado = f"O aluno foi reprovado com {M:.2f} pontos na média anual."

        return render_template('index.html', resultado=resultado, NG=NG)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)