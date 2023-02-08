from cachetools import cached
from flask import Flask
from flask_bcrypt import Bcrypt


@cached({})
def get_app():
    app = Flask("app")

    return app


@cached({})
def get_bcrypt():
    bcrypt = Bcrypt(get_app())

    return bcrypt
