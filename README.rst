Django generator
================

Application aim to provide an interface to quick start a django application.


Installing the package
----------------------

.. code-block:: bash

    $ mkvirtualenv djangogenerator
    $ git clone https://github.com/gotlium/djangogenerator
    $ cd djangogenerator/
    $ pip install -r requirements.txt


Configuration
-------------

After installation, you need to configure and sync database. Do not forget
create root user on synchronization step.

.. code-block:: python

    $ python manage.py syncdb
    $ python manage.py migrate


Usage
-----
Now you can run and use djangogenerator.

.. code-block:: python

    $ python manage.py runserver_plus


.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/djangogenerator/trend.png
   :alt: Bitdeli badge
   :target: https://bitdeli.com/free

