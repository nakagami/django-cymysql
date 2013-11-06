django-cymysql
==============

django mysql database backend with cymysql

------------

* Django 1.6
* CyMySQL (https://github.com/nakagami/CyMySQL) 0.7.x

Installation
------------

::

    $ git clone https://github.com/nakagami/django-cymysql
    $ cd django-cymysql
    $ python setup.py install

Database
------------

* Create database (set default character set to 'utf8')

::

    mysql> create database some_what_database default character set utf8;

Settings
------------

::

    DATABASES = {
        'default': {
            'ENGINE': 'mysql_cymysql',
            'NAME': 'some_what_database',
            'HOST': ...,
            'USER': ...,
            'PASSWORD': ...,
        }
    }


