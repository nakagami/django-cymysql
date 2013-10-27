django-cymysql
==============

django mysql database backend with cymysql

------------

* Django 1.6
* CyMySQL (https://github.com/nakagami/CyMySQL) 0.7

Installation
------------

::

    $ git clone https://github.com/nakagami/django-cymysql
    $ cd django-cymysql
    $ python setup.py install

Settings
------------

::

    DATABASES = {
        'default': {
            'ENGINE': 'mysql_cymysql',
            'HOST': ...,
            'USER': ...,
            'PASSWORD': ...,
        }
    }


