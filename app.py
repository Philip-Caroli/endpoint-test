from bottle import Bottle, route, run, template, static_file, request, error, hook, get, post, server_names
import bottle
import datetime
import fabkalendergenerator

@route('/static/<type>/<filename>')
def serve_css(type, filename):
    return static_file(filename, root=type+'/')


@get('/')
def main_menu():
    now = datetime.datetime.now()
    print("HTTP GET")

@post('/')
def main_menu():
    now = datetime.datetime.now()
    print("HTTP POST")


run(host='0.0.0.0', port=10126)
