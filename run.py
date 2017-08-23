import traceback

from flask import Flask, render_template
import configparser
from analyse.analyse import Analyse
from json_out.output import JsonOuter

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

json_outer = JsonOuter()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/get_count')
def get_count():
    analyse = Analyse()
    result = {}
    try:
        result = analyse.get_user_num()
        if not result:
            result = {}
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_sex_count')
def get_sex():
    analyse = Analyse()
    result = {}
    try:
        result = analyse.get_sex()
        if not result:
            result = None
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_school_count')
def get_school():
    analyse = Analyse()
    result = []
    try:
        result = analyse.get_school_count()
        if not result:
            result = []
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_trade_count')
def get_trade():
    analyse = Analyse()
    result = []
    try:
        result = analyse.get_trade_count()
        if not result:
            result = []
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_location_count')
def get_location():
    analyse = Analyse()
    result = []
    try:
        result = analyse.get_location_count()
        if not result:
            result = []
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_company_count')
def get_company():
    analyse = Analyse()
    result = []
    try:
        result = analyse.get_company_count()
        if not result:
            result = []
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_agree_count')
def get_agree():
    analyse = Analyse()
    result = {}
    try:
        result = analyse.get_agree_count()
        if not result:
            result = {}
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


@app.route('/get_follower_count')
def get_follower():
    analyse = Analyse()
    result = {}
    try:
        result = analyse.get_follower_count()
        if not result:
            result = {}
    except Exception as err:
        traceback.print_exc()
        print(err)
    return json_outer.data(result)


if __name__ == '__main__':
    app.run(host=config.get('sys', 'listen_ip'), port=config.get('sys', 'listen_port'))
