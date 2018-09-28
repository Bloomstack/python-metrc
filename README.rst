============
Python METRC
============

A light Python wrapper around the METRC Web API

.. image:: https://img.shields.io/pypi/v/python_metrc.svg
        :target: https://pypi.python.org/pypi/python_metrc

.. image:: https://img.shields.io/travis/DigiThinkIT/python_metrc.svg
        :target: https://travis-ci.org/DigiThinkIT/python_metrc

Getting Started
---------------

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

Installing
~~~~~~~~~~

::

   $ pip install python_metrc

Running the tests
~~~~~~~~~~~~~~~~~

::

   cd python_metrc
   pytest

Documentation
-------------

To generate and call the endpoint - ``https://sandbox-api-ca.metrc.com/transfers/v1/delivery/packages/states`` - you can use any of the following combinations:

::

    >>> from python_metrc import METRC
    >>> metrc = METRC('https://sandbox-api-ca.metrc.com', vendor_key={VENDOR_KEY}, user_key={USER_KEY}, license_number={LICENSE_NUMBER})
    >>> metrc.transfers('delivery').packages('states').get()
    <Response [200]>
    >>> metrc.transfers.delivery.packages('states').get()
    <Response [200]>
    >>> metrc.transfers.delivery.packages.states.get()
    <Response [200]>
    >>> metrc.transfers('delivery', 'packages', 'states').get()
    <Response [200]>

The ``METRC`` class instance provides the ``GET``, ``POST`` and ``DELETE`` HTTP methods as binded on itself. The return type is the ``requests`` module's ``Response`` object.

Contributing
------------

Please read the `Contribution`_ guidelines for details on our code of conduct, and the process for submitting pull requests to us.

Authors
-------

See the list of `contributors`_ who participated in this project.

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file for details

Acknowledgments
---------------

-  `Hammock`_ - Used to generate RESTful URLs

.. _Hammock: https://github.com/kadirpekel/hammock
.. _Contribution: https://github.com/DigiThinkIT/python-metrc/blob/master/CONTRIBUTING.rst
.. _tags on this repository: https://github.com/DigiThinkIT/python-metrc/tags
.. _contributors: https://github.com/DigiThinkIT/python-metrc/contributors
.. _LICENSE: https://github.com/DigiThinkIT/python-metrc/blob/master/LICENSE
