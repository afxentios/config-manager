from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name='config-manager',
      version='1.1.2',
      description='A basic configuration reader and manager for python projects',
      long_description=readme(),
      url='https://github.com/afxentios/config-manager',
      license='MIT',
      author='Afxentios Hadjiminas',
      author_email='afxentios@hadjimina.com',
      keywords=["configuration", "management"],
      packages=find_packages(),
      install_requires=['pyyaml',
                        'simplejson'],
      extras_require={
          'test': ['unittest2',
                   'mock']
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules']
      )
