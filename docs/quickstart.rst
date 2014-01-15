.. _quickstart:

Quickstart
==========

This guide assumes you have successfully installed Flask-YourExt and a working
understanding of Flask. If not, follow the installation steps and read about
Flask at http://flask.pocoo.org/docs/.


A Minimal Example
-----------------

A minimal Flask-YourExt usage example looks like this. First create the
application and initialize the extension:

>>> from flask import Flask
>>> from flask_yourext import YourExt
>>> app = Flask('myapp')
>>> ext = YourExt(app=app)

Some Extended Example
---------------------
Flask-YourExt also has support for CHANGEME

.. literalinclude:: ../tests/helpers.py
