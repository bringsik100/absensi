# -*- coding: utf-8 -*-
"""
    Setup file for mobile.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

setup(name='Absensi',
      version='0.1.3',
      description='skrip python untuk membuat laporan berformat excel yang tampilannya sama seperti keluaran dari aplikasi attendance manager',
      long_description='Really, the funniest around.',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
		'Environment :: Console',
        'Programming Language :: Python :: 3.4',
		'Intended Audience :: Other Audience',
		'Natural Language :: Indonesian',
		'Operating System :: OS Independent',
        'Topic :: Text Processing',
	  url='http://github.com/bringsik100/absensi',
      author='bringsik100',
      author_email='dont.mail@me.com',
      license='MIT',
      packages=['absensi'],
      install_requires=[
		  'openpyxl',
      ],
      zip_safe=False)

if __name__ == "__main__":
    setup(use_pyscaffold=True)
