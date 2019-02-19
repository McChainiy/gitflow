from flask import Flask, url_for
import os

app = Flask(__name__)
count = 0


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/image_sample')
def sova():
    return 'Супрематическое пространство</br>{}'.format(
        '''<img src="{}" alt="здесь могла быть ваше изображение">'''.format(
            url_for('static', filename='img/sova.jpeg')))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
