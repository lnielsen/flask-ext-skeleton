# -*- coding: utf-8 -*-
##
## This file is part of Flask-YourExt
## Copyright (C) 2014 CERN.
##
## Flask-YourExt is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Flask-YourExt is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Flask-YourExt; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

"""
Amodule User Documentation
===========================

Your user documentation goes here. This documentation is included
in the Sphinx documentation.

Doc tests are written like this:

>>> from flask import Flask, Blueprint
>>> from flask_yourext import YourExt
>>> def create_app():
...     app = Flask('myapp')
...     ext = YourExt(app=app)
...     return app
>>> app = create_app()

You run doc tests like this::

    pip install Sphinx
    python setup.py build_sphinx -b doctest

By default Tox will run both unit tests and doc tests in all.

Subheading
^^^^^^^^^^
Some more documentation
"""

from __future__ import absolute_import


class AClass(object):
    """
    API documentation goes here.

    :param avar: Description of avar
    """
    def __init__(self, avar):
        self.a = avar
