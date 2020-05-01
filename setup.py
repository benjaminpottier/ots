from setuptools import setup

setup(
    name='ots',
    version='1.0',
    description='A cli for onetimesecret.com',
    author='Ben Pottier',
    author_email='benpottier@gmail.com',
    packages=['ots'],
    install_requires=['fire'],
    scripts=['scripts/otscli.py']
)
