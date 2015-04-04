django-cymysql
==============

Django mysql database backend for cymysql

------------

* Django 1.6 ,1.7 and 1.8
* CyMySQL (https://github.com/nakagami/CyMySQL) 0.8.x+

Installation
------------

::

    $ pip install cymysql
    $ pip install django-cymysql

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

If you want to use south::

   SOUTH_DATABASE_ADAPTERS = {
       'default': "south.db.mysql"
   }
