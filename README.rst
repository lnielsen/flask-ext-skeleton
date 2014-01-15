========================
Flask Extension Skeleton
========================

.. image:: https://travis-ci.org/inveniosoftware/flask-ext-skeleton.png?branch=master
    :target: https://travis-ci.org/inveniosoftware/flask-ext-skeleton
.. image:: https://coveralls.io/repos/inveniosoftware/flask-ext-skeleton/badge.png?branch=master
    :target: https://coveralls.io/r/inveniosoftware/flask-ext-skeleton

Skeleton for starting a new Flask extension according to best practices:

 * Proper Python packaging including best practice for how to provide versioning.
 * Examples of unit tests and doc tests.
 * Examples of user and API documentation.
 * Example of Flask extension class.
 * Documentation using Sphinx and with the default Flask theme.
 * Test coverage and documentation coverage.
 * Travis CI configuration with support for coveralls (test coverage reporting).
 * Python 2.6, 2.7 and Python 3.3 compatibility using six library and easy testing via Tox.


Get started
===========
To start your new Flask extension::

    git clone https://github.com/inveniosoftware/flask-ext-skeleton.git flask-<newname>
    cd flask-<newname>
    rm -Rf docs/_themes/

    # Search and replace
    git ls-files | grep -v docs/_themes | xargs sed -i -e 's/YourExt/<NewName>/g'
    git ls-files | grep -v docs/_themes | xargs sed -i -e 's/yourext/<newname>/g'

    # Rename extension
    mv flask_yourext flask_<newname>

    # Remove this README, and replace with your extension.
    rm README.rst
    mv README-YourExt.rst README.rst

    # Remove old git repository
    rm -Rf .git .gitmodules

    # Create new git repository
    git init .
    git a -A
    git submodule add https://github.com/mitsuhiko/flask-sphinx-themes docs/_themes/
    git ci -m "Initial commit"

    # List files you need to edit
    git grep CHANGEME

Here is a quick overview over what you can do locally with your newly created extension::

    $ mkvirtualenv flask-newname
    (flask-newname)$ pip install Sphinx coverage
    (flask-newname)$ python setup.py develop

    # Run unit tests
    (flask-newname)$ python setup.py test

    # Run unit tests with test coverage
    (flask-newname)$ source run-tests.sh

    # Doc tests
    (flask-newname)$ python setup.py build_sphinx -b doctest

    # Build documentation (docs/_build/html/index.html)
    (flask-newname)$ python setup.py build_sphinx

    # Documentation coverage
    (flask-newname)$ python setup.py build_sphinx -b coverage && cat docs/_build/coverage/python.txt

    # Run unit and doc tests in Python 2.6, Python 2.7 and Python 3.3
    (flask-newname)$ tox


The default extension include examples of additional package and modules (apackage and amodule). To remove them, simply delete them and update setup.py, docs/userguide.rst and docs/api.rst.

Testing
=======
Running the tests are as simple as: ::

    python setup.py test

or (to also show test coverage) ::

    source run-tests.sh

License
=======
Copyright (C) 2014 CERN.

Flask-YourExt is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

Flask-YourExt is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Flask-YourExt; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

In applying this licence, CERN does not waive the privileges and immunities granted to it by virtue of its status as an Intergovernmental Organization or submit itself to any jurisdiction.

.. image:: https://d2weczhvl823v0.cloudfront.net/inveniosoftware/flask-ext-skeleton/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free