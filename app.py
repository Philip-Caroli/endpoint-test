from bottle import Bottle, route, run, template, static_file, request, error, hook, get, post, server_names
import bottle
import datetime
import logging
logging.basicConfig(level=logging.INFO, filename="log/log.txt", filemode="a+",
                    format='%(asctime)s - %(message)s')

@route('/static/<type>/<filename>')
def serve_css(type, filename):
    return static_file(filename, root=type+'/')


@get('/')
def main_menu():
    now = datetime.datetime.now()
    logging.info("get request recieved")
    return "get processed"

@post('/')
def main_menu():
    now = datetime.datetime.now()
    logging.info("post request recieved")
    return "post processed"

logging.info("Starting Service")
run(host='0.0.0.0', port=10126)
logging.info("Finishing Service")