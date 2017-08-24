siphashc
========

.. image:: https://travis-ci.org/WeblateOrg/siphashc.svg?branch=master
    :target: https://travis-ci.org/WeblateOrg/siphashc

.. image:: https://ci.appveyor.com/api/projects/status/kgeohtb6as3xd9b7/branch/master?svg=true
    :target: https://ci.appveyor.com/project/nijel/siphashc-merge/branch/master

.. image:: https://api.codacy.com/project/badge/Grade/33758f86fbf44e929d85f47390093771    
    :target: https://www.codacy.com/app/Weblate/siphashc

Introduction
~~~~~~~~~~~~

siphashc is a python c-module for
`siphash <https://131002.net/siphash/>`__, based on `floodberry's
version <https://github.com/floodyberry/siphash>`__.

It was merged from two versions of the module:

-  https://github.com/cactus/siphashc
-  https://github.com/carlopires/siphashc3

Usage
~~~~~

Python 2
^^^^^^^^

.. code:: python

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048L

Python 3
^^^^^^^^

.. code:: python

    >>> from siphashc import siphash
    >>> siphash('sixteencharstrng', 'i need a hash of this')
    10796923698683394048

License
~~~~~~~

Released under the `MIT
license <http://www.opensource.org/licenses/mit-license.php>`__. See
``LICENSE.md`` file for details.
