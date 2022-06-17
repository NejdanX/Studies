from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def slogan():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion():
    with open('cgi-bin/hello_mars.html', 'r', encoding='utf-8') as html_file:
        return html_file.read()


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def selection():
    if request.method == 'GET':
        with open('cgi-bin/form.html', 'r', encoding='utf-8') as html_file:
            return html_file.read()
    else:
        print(request.form['surname'])
        print(request.files['file'].read())
        return 'success'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
