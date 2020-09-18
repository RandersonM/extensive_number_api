# coding: utf-8
from flask import Flask, render_template
from assets import strings

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<number>')
def getExtensiveNumber(number):
    """
    De acordo com o parâmetro number realiza 3 divisão para saber se o numero está na casa dos milhar, centena ou decimal
    :param number:
    :return:
    """
    try:
        path = "menos " if int(number) < 0 else ""
        number = abs(int(number))
    except ValueError or TypeError:
        return {"erro" : strings.type_value_error_msg }

    path += numberToExtensive(((number // 1000) % 100), strings.milhar)

    if number > 1000 and number % 1000:
        path += "e "

    path += strings.centena[((number // 100) % 10)] if number != 100 else "cem"

    if number > 100 and number % 100:
        path += "e "

    path += numberToExtensive((number % 100), "")

    if number == 0:
        path = "zero"

    context = {"extenso": path}
    return context


def numberToExtensive(number, place):
    """
    :param number: numero a ser convertido para forma extensiva no português
    :param place: posição decimal do numero
    :return: string com o nome extensivo do parametro number com a casa
    """
    extensive = ""
    if number > 19:
        extensive += strings.dezenas[number // 10]
        extensive += "e " if number % 10 != 0 else ""
        extensive += strings.unidades[number % 10]
    else:
        extensive += strings.unidades[number]

    if number:
        extensive += place

    return extensive


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
