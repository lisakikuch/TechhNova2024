import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(app.py, instance_relative_config=True)
    app.config.from_mappig(
            SECRET_KEY='dev'
            )
    if test_config is None:
        app.config.from_mapping(test_config)

    try: 
        os.makedirs(app.instancae_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
