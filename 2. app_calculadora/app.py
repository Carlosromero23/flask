# Importamos las clase y métodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo de forma n1, n2 son pasados 
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # Realizamos operaciones aritméticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2 if num2 != 0 else 'Error: División por cero'
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_division=division)
    
    return render_template('index.html')

@app.route('/divisa', methods=['GET', 'POST'])
def divisas():
    if request.method == "POST":
        # Valores que recibo de forma d1 son pasados 
        div = float(request.form.get('d1'))
        # Realizamos operaciones de divisas
        divisa = div * 4213 
        euros= div/4500
        return render_template('divisa.html', total_divisa=divisa,
                                              total_euros=euros)
    
    return render_template('divisa.html')

@app.route('/longitudes', methods=['GET', 'POST'])
def convertir_metros():
    if request.method == "POST":
        # valores en metros
        metros = float(request.form.get('metros'))
        #operaciones
        centimetros = metros * 100
        kilometros = metros / 1000
        return render_template('longitudes.html', total_centimetros=centimetros,
                                        total_kilometros=kilometros)

    return render_template('longitudes.html')

if __name__ == "__main__":
    app.run(debug=True)
