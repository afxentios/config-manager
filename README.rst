config-manager: Read and manage configuration data for your application
=======================================================================

Build Status
------------

|travis status| |coverage| |health|

Project details
---------------

|license| |pypi|

.. |travis status| image:: https://travis-ci.org/afxentios/config-manager.svg?branch=master
   :target: https://travis-ci.org/afxentios/config-manager
   :alt: Travis-CI build status
.. |coverage| image:: https://coveralls.io/repos/github/afxentios/config-manager/badge.svg
   :target: https://coveralls.io/github/afxentios/config-manager
   :alt: Code Coverage
.. |health| image:: https://landscape.io/github/afxentios/config-manager/master/landscape.svg?style=flat
   :target: https://landscape.io/github/afxentios/config-manager/master
   :alt: Code Health
.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/afxentios/config-manager/blob/master/LICENSE.txt
   :alt: License
.. |pypi| image:: https://badge.fury.io/py/config-manager.svg
   :target: https://badge.fury.io/py/config-manager
   :alt: Pypi Version


Description
-----------

The **config-manager** package is a basic configuration reader and manager. It reads the configuration data from
an external YAML or JSON file and it injects this data into the application that is called from. It's currently
tested on Python 2.7.

- `Issue tracker`_
- `Changelog`_


Installation
------------

::

  pip install config-manager

or

download the `latest release`_ and run

::

  python setup.py install


Usage
-----

::

  #configs.yaml contains the configuration data

  from config_manager import ConfigManager
  confman = ConfigManager(config_file_path='/path/to/configs.yaml', defaults={'maintenance':'False'}, required=['maintenance'])
  maintenance = confman['maintenance']


License
-------

This project is licensed under the MIT license.

.. _Changelog: https://github.com/afxentios/config-manager/blob/master/CHANGELOG.md
.. _Issue tracker: https://github.com/afxentios/config-manager/issues
.. _latest release: https://github.com/afxentios/config-manager/releases
