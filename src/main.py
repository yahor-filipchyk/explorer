
import os
from bottle import post, route, run, static_file, template
import dao.data_provider as dp

def get_files_contents(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents

@route('/static/styles/<file>')
def get_style(file):
    return static_file(file, os.path.join(os.path.dirname(__file__), 'static/styles/'))

@route('/static/scripts/<file>')
def get_style(file):
    return static_file(file, os.path.join(os.path.dirname(__file__), 'static/scripts/'))

@route('/files')
def index():
    return template(get_files_contents(os.path.join(os.path.dirname(__file__), 'static/index.html')))

@post('/files/list/<path:path>')
def get_files_list(path):
    return dp.get_files(path)

run(host='localhost', port=8000)
