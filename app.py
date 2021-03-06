"""
This script runs the application using a development server.
"""
# import locale

from flask import Flask

from views.public import app as public_app
from views.admin import APP as admin_app
from settings.extensions import ExtensionsManager

APP = Flask(__name__)
ExtensionsManager.auto_configure(APP)

APP.register_blueprint(public_app)
APP.register_blueprint(admin_app)

PUBLIC_HOST = '0.0.0.0'
PUBLIC_PORT = 80
DEV_HOST = 'localhost'
DEV_PORT = 4444

if __name__ == '__main__':

    try:
        APP.run(PUBLIC_HOST, PUBLIC_PORT)
    except PermissionError:
        print('DEVELOPMENT MODE: running at localhost only!!!')
        APP.jinja_env.auto_reload = True
        APP.config['TEMPLATES_AUTO_RELOAD'] = True
        APP.run(DEV_HOST, DEV_PORT, debug=True)
