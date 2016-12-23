from setuptools import setup, find_packages

import config_manager


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name='config-manager',
      version=config_manager.__version__,
      description='A basic configuration reader and manager for python projects',
      long_description=readme(),
      url='https://github.com/afxentios/config-manager',
      license='MIT',
      author=config_manager.__author__,
      author_email='afxentios@hadjimina.com',
      keywords=["configuration", "management"],
      packages=find_packages(),
      install_requires=['PyYAML', 'simplejson', 'mock'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules']
      )
