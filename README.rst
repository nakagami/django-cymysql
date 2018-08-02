django-cymysql
==============

Django mysql database backend for cymysql

Requirements
-------------

* Django 1.10, 1.11, 2.0, 2.1
* CyMySQL (https://github.com/nakagami/CyMySQL) 0.9.3+

Installation
------------

Install with Django x.y.z.

::

    $ pip install cymysql
    $ pip install "django-cymysql>=x.y,<x.y+1"
    $ pip install Django==x.y.z

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
