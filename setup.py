#!/usr/bin/env python
"""
Django database backend for cymysql
"""
from distutils.core import setup, Command

classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Database',
]

setup(name='django-cymysql', 
        version='0.1.0',
        description = __doc__, 
        url='https://github.com/nakagami/django-cymysql/',
        classifiers=classifiers,
        keywords=['MySQL', 'cymysql'],
        license='BSD',
        author='Hajime Nakagami',
        author_email='nakagami@gmail.com',
        packages = ['mysql_cymysql'],
        long_description=__doc__,
)
