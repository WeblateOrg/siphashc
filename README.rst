.. image:: https://s.weblate.org/cdn/Logo-Darktext-borders.png
   :alt: Weblate
   :target: https://weblate.org/
   :height: 80px

**Weblate is libre software web-based continuous localization system,
used by over 2500 libre projects and companies in more than 165 countries.**

siphashc is a Python module (in c) for siphash-2-4

.. image:: https://img.shields.io/pypi/v/siphashc.svg
    :target: https://pypi.python.org/pypi/siphashc
    :alt: PyPI package

Installation
~~~~~~~~~~~~

Install using pip:

.. code-block:: sh

    pip install siphashc

Sources are available at <https://github.com/WeblateOrg/siphashc>.

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

.. code:: pycon

    >>> from siphashc import siphash
    >>> siphash("sixteencharstrng", "i need a hash of this")
    10796923698683394048

License
~~~~~~~

Released under the `ISC
license <https://choosealicense.com/licenses/isc/>`__. See
``LICENSE.md`` file for details.

Contributing
~~~~~~~~~~~~

Contributions are welcome! See `documentation <https://docs.weblate.org/en/latest/contributing/modules.html>`__ for more information.
