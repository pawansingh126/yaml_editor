##############################################################################
#
# Author  : Pawan Singh Pal
# Email   : pawansingh126@gmail.com
# Date    : Oct 2018
#
##############################################################################


import click
import json
import os
import socket
import yaml

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app_path  = os.path.dirname(os.path.abspath(__file__))

app = Flask('Yaml Editor!',
            template_folder=os.path.join(app_path, 'templates'),
            static_folder=os.path.join(app_path, 'static'))
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders index page to edit provided yaml file."""
    with open(app.config['YAML_FILE_OBJ']) as file_obj:
        data = yaml.load(file_obj, Loader=yaml.Loader)
    return render_template('yaml.html',
                           data=json.dumps(data),
                           change_str=app.config['STRING_TO_CHANGE'])

@app.route('/tree', methods=['GET', 'POST'])
def tree():
    """Renders tree view page to edit provided yaml file."""
    with open(app.config['YAML_FILE_OBJ']) as file_obj:
        data = yaml.load(file_obj, Loader=yaml.Loader)
    return render_template('treeyaml.html',
                           data=data, datastr=json.dumps(data),
                           change_str=app.config['STRING_TO_CHANGE'])

@app.route('/save', methods=['POST'])
def save():
    """Save current progress on file."""
    out = request.json.get('yaml_data')
    with open(app.config['YAML_FILE_OBJ'], 'w') as file_obj:
        yaml.dump(out, file_obj, default_flow_style=False)
    return "Data saved successfully!"

@app.route('/saveExit', methods=['POST'])
def save_exit():
    """Save current progress on file and shuts down the server."""
    out = request.json.get('yaml_data')
    with open(app.config['YAML_FILE_OBJ'], 'w') as file_obj:
        yaml.dump(out, file_obj, default_flow_style=False)
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    return "Saved successfully, Shutting down app! You may close the tab!"

@app.errorhandler(404)
def page_not_found(e):
    """Serves 404 error."""
    return '<h1>404: Page not Found!</h1>'

def run(*args, **kwargs):
    """Starts the server."""
    port = kwargs.get('port', None)
    if not port:
        port = 8161
    app.run(host='0.0.0.0', port=port, debug=False)


@click.command()
@click.option(
    '--file',
    '-f',
    required=True,
    type=click.Path(exists=True),
    multiple=False,
    help="Path with file name to the intermediary yaml file."
)
@click.option(
    '--port',
    '-p',
    default=8161,
    type=click.INT,
    multiple=False,
    help="Optional port parameter to run Flask on."
)
@click.option(
    '--string',
    '-s',
    default='#CHANGE_ME',
    type=click.STRING,
    multiple=False,
    help="Text which is required to be changed on yaml file."
)
def main(*args, **kwargs):
    print("Please go to http://{0}:{1}/ to edit your yaml file.".format(
        socket.gethostbyname(socket.gethostname()), kwargs['port']))
    app.config['YAML_FILE_OBJ'] = kwargs['file']
    app.config['STRING_TO_CHANGE'] = kwargs['string']
    run(kwargs)

if __name__=='__main__':
    """Invoked when used as a script."""
    main()
